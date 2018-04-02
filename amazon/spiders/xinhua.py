import random
from urllib import parse
import scrapy
import time
from scrapy_redis.spiders import RedisSpider
from amazon.items import XinhuaItem

class XinhuaSpider(RedisSpider):
    name = "xinhua"
    allowed_domains = ["www.amazon.cn"]
    # 起始首页需要定制
    redis_key = 'xinhua:start_urls'
    # start_urls = ['https://www.amazon.cn/gp/node/index.html?ie=UTF8&merchant=A33E54V2WD1T67']

    def parse(self, response):
        # 提取各类商品搜索页链接
        urls = response.css('.widgetSideBox div')
        for result in urls:
            commoditytype_url = result.css('a::attr(href)').extract_first()
            time.sleep(random.uniform(0.6,1.2))
            yield scrapy.Request(url=commoditytype_url,callback=self.parse_departments)
            # break

    def parse_departments(self,response):
        # 商品搜索页最大页码
        part1_url = response.css('#pagnNextLink::attr(href)').re('(.*?sr_pg_.*?)/.*')[0]
        part2_url = response.css('#pagnNextLink::attr(href)').re('.*?(\?.*?UTF8).*')[0]
        start_url = part1_url+part2_url
        # 小于6页last_page不存在
        last_page = response.css(".pagnDisabled::text").extract_first()
        if last_page:
            for page_num in range(1,int(last_page+1)):
                url = start_url.replace('page=2','page='+str(page_num)).replace('sr_pg_2','sr_pg_'+str(page_num))
                yield scrapy.Request(url=parse.urljoin(response.url,url),callback=self.parse_search_page)
        else:
            last_page = response.xpath("//*[@id='pagn']/span[-2]/text()").extract_first()
            for page_num in range(1,int(last_page+1)):
                url = start_url.replace('page=2','page='+str(page_num)).replace('sr_pg_2','sr_pg_'+str(page_num))
                yield scrapy.Request(url=parse.urljoin(response.url,url),callback=self.parse_search_page)


    def parse_search_page(self,response):
        # 提取相关商品信息
        xinhuaitem = XinhuaItem()
        pages = response.css('.s-result-item.celwidget ')
        for page in pages:
            xinhuaitem['commodity_img'] = page.css('.a-spacing-base .a-spacing-none img::attr(src)').extract_first()
            xinhuaitem['commodity_url'] = page.css('.s-access-detail-page::attr(href)').re('(^https://www.amazon.cn/.*?UTF8).*')[0]
            xinhuaitem['commodity_name'] = page.css('.s-access-detail-page::attr(title)').extract_first()
            xinhuaitem['commodity_price'] = page.css('span.a-size-base.a-color-price.s-price.a-text-bold::text').extract_first()
            if xinhuaitem['commodity_price']:
                xinhuaitem['commodity_price'] = xinhuaitem['commodity_price'].replace('￥','')
            else:
                xinhuaitem['commodity_price'] = '0.00'
            xinhuaitem['commodity_ASIN'] = page.css('.s-result-item::attr(data-asin)').extract_first()
            xinhuaitem['commodity_tag1'] = response.css('.a-link-normal.a-color-base.a-text-bold.a-text-normal::text').extract()[1]
            tags = response.css('.a-link-normal.a-color-base.a-text-bold.a-text-normal::text').extract()
            if len(tags) > 2:
                xinhuaitem['commodity_tag2'] =tags[2]
            else:
                xinhuaitem['commodity_tag2'] = response.css('.a-color-state.a-text-bold::text').extract_first()
            xinhuaitem['commodity_seller'] = response.css('.a-link-normal.a-color-base.a-text-bold.a-text-normal::text').extract_first().replace(' 店面','')
            yield xinhuaitem




