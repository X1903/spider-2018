# -*- coding: utf-8 -*-

import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

from scrapy_redis.spiders import RedisCrawlSpider

from Amz.items import Amazon_Commet_Item


class BaiduSpider(RedisCrawlSpider):
    name = 'Amazon'

    redis_key = 'Amazon_spider:start_urls'

    def parse(self, response):
        print(response.url)

        Reviews = response.xpath('//*[@id="cm_cr-review_list"]/div[@data-hook="review"]')
        item = Amazon_Commet_Item()
        Reviewer_lists = []
        for Review in Reviews:
            Reviewer_dict = {}
            Reviewer_dict['Reviewer'] = Review.xpath('./div/div[2]/span/a/text()').extract_first()  # 评价人
            Reviewer_dict['ReviewerCustomerUrl'] = Review.xpath('./div/div[2]/span/a/@href').extract_first()  # 评价人页面url
            Reviewer_dict['ReviewCustomerUrlId'] = Review.xpath('./div/div[2]/span/a/@href').extract_first()  # 评价人页面id
            Reviewer_dict['Star'] = Review.xpath('./div/div[1]/a/i/span/text()').extract_first()[0]  # 星级
            Reviewer_dict['CommentId'] = Review.xpath('./@id').extract_first()  # 评价id
            Reviewer_dict['CommentTime'] = Review.xpath(
                './div/div[2]/span[@data-hook="review-date"]/text()').extract_first()  # 评价时间
            Reviewer_dict['ReviewContent'] = ','.join(Review.xpath('./div/div[4]/span/text()').extract())  # 评价内容
            ReviewImages = Review.xpath('./div/div[6]/div[1]/img/@src').extract()  # 评价照片
            if ReviewImages:
                Reviewer_dict['ReviewImages'] = ','.join(ReviewImages)
            else:
                Reviewer_dict['ReviewImages'] = None
            VerifiedPurchases = Review.xpath('./div/div[3]/span/a/span/text()').extract()  # 确认购买
            if VerifiedPurchases:
                Reviewer_dict['VerifiedPurchases'] = True
            else:
                Reviewer_dict['VerifiedPurchases'] = False

            Reviewer_lists.append(Reviewer_dict)
        item['suoyou'] = Reviewer_lists

        yield item
