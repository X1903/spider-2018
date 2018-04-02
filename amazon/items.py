import datetime
import scrapy
from amazon.settings import SQL_DATETIME_FORMAT

class XinhuaItem(scrapy.Item):
    commodity_url = scrapy.Field()
    commodity_img = scrapy.Field()
    commodity_name = scrapy.Field()
    commodity_price = scrapy.Field()
    commodity_ASIN = scrapy.Field()
    commodity_seller = scrapy.Field()
    commodity_tag1 = scrapy.Field()
    commodity_tag2 = scrapy.Field()

    def get_insert_sql(self):
        #插入知乎question表的sql语句
        insert_sql = '''
            insert into WenXuan_bookstore(commodity_seller,commodity_ASIN,commodity_name,commodity_price,commodity_tag1,commodity_tag2,
              commodity_url,commodity_img,crawl_time
              )
            VALUE (%s,%s,%s,%s,%s,%s,%s,%s,%s)
            ON DUPLICATE KEY UPDATE commodity_price=VALUES(commodity_price)
        '''
        commodity_seller = self['commodity_seller']
        commodity_ASIN = self['commodity_ASIN']
        commodity_name = self['commodity_name']
        commodity_price = self['commodity_price']
        commodity_tag1 = self['commodity_tag1']
        commodity_tag2 = self['commodity_tag2']
        commodity_url = self['commodity_url']
        commodity_img = self['commodity_img']
        crawl_time = datetime.datetime.now().strftime(SQL_DATETIME_FORMAT)

        params = (commodity_seller,commodity_ASIN,commodity_name,commodity_price,commodity_tag1,commodity_tag2,commodity_url,commodity_img,crawl_time)

        return insert_sql, params

