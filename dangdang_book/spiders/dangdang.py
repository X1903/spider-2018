# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider
from copy import deepcopy

class DangdangSpider(RedisSpider):
    name = 'dangdang'
    allowed_domains = ['dangdang.com']
    # start_urls = ['http://book.dangdang.com/']
    redis_key = "dangdang"

    def parse(self, response):
        #大分类的列表
        div_list = response.xpath("//div[@class='con flq_body']/div")[2:-1]
        print(len(div_list),"-"*100)
        for div in div_list:
            item = {}
            item["b_cate"] = div.xpath("./dl[@class='primary_dl']/dt//text()").extract()
            #中间分类的列表
            dl_list = div.xpath(".//div[@class='col eject_left']/dl")
            print(len(dl_list), "*" * 100)

            for dl in dl_list:
                item["m_cate"] = dl.xpath("./dt/a/@title").extract_first()
                #小分类的列表
                a_list = dl.xpath("./dd/a")
                print(len(a_list), "+" * 100)

                for a in a_list:
                    item["s_cate"] = a.xpath("./@title").extract_first()
                    item["s_href"]= a.xpath("./@href").extract_first()
                    if item["s_href"] is not None:
                        #发送小分类url的请求，到达列表页
                        yield scrapy.Request(
                            item["s_href"],
                            callback=self.parse_book_list,
                            meta={"item":deepcopy(item)}
                        )

    def parse_book_list(self,response):
        item = response.meta["item"]
        #活去图书列表的分组
        li_list =response.xpath("//ul[@class='bigimg']/li")
        for li in li_list:
            item["book_name"]=li.xpath("./a/@title").extract_first()
            item["book_img"] = li.xpath("./a/img/@src").extract_first()
            item["book_pirce"] = li.xpath(".//span[@class='search_now_price']/text()").extract_first()
            item["book_author"] = li.xpath(".//p[@class='search_book_author']/span[1]/a/text()").extract()
            item["book_press"] = li.xpath(".//p[@class='search_book_author']/span[3]/a/text()").extract_first()
            print(item)

        #列表页翻页
        next_url_temp = response.xpath("//a[@title='下一页']/@href").extract_first()
        if next_url_temp is not None:
            next_url = "http://category.dangdang.com"+next_url_temp
            yield  scrapy.Request(
                next_url,
                callback=self.parse_book_list,
                meta = {"item":item}
            )


