# -*- coding: utf-8 -*-
import scrapy
from pyquery import PyQuery as pq
from copy import deepcopy
from dongguan.items import DongguanItem
import copy


class DgHouseSpider(scrapy.Spider):
    name = 'dg_house'
    # allowed_domains = ['*']
    start_urls = ['http://dgfc.dg.gov.cn/dgwebsite_v2/Vendition/ProjectInfo.aspx?new=1']


    base_url = "http://dgfc.dg.gov.cn/dgwebsite_v2/Vendition/"

    def parse(self, response):
        doc = pq(response.text)
        tr_list = doc("#resultTable tr:gt(0)").items()   # 获取所有的tr, 第一行不要
        for tr in tr_list:
            tr_url = self.base_url + tr('td:eq(0) a').attr('href')  # 取第一个td的href
            yield scrapy.Request(
                tr_url,
                callback=self.list_detail
            )

    def list_detail(self, response):
        item = DongguanItem()
        doc = pq(response.text)
        tr_list = doc("#houseTable_1 tr:gt(0)").items()  # 获取所有的tr, 第一行不要
        for tr in tr_list:
            item['projectUrl'] = self.base_url + tr('td:eq(1) a').attr('href')  # 取第一个td的href
            item['projectTitle'] = tr('td:eq(1) a').text()
            yield scrapy.Request(
                item['projectUrl'],
                callback=self.floorsDetail,
                meta={'item':copy.deepcopy(item)}
            )


    def floorsDetail(self, response):
        item = response.meta['item']
        doc = pq(response.text)
        floorsInfo = []
        tr_list = doc('#roomTable tr:gt(0)').remove('font').items()

        for tr in tr_list:
            floorInfo = {}

            rooms = tr('table tr td').items()
            RoomsInfo = []
            for room in rooms:   # 获取房间信息
                RoomInfo = {}
                RoomInfo['room_num'] = room.text()
                RoomInfo['room_info'] = room.attr('title')
                RoomsInfo.append(RoomInfo)


            floorInfo['RoomsInfo'] = RoomsInfo
            floorInfo['floor_num'] = tr.remove('td:gt(0)').text()    # 获取楼层
            floorsInfo.append(floorInfo)
        item['projectFloors'] = floorsInfo

        print(item)

