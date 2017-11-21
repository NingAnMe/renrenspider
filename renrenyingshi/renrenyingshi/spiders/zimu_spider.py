# -*- coding: utf-8 -*-
import scrapy
import time

from renrenyingshi.items import ZimuDetailItem


class ZimuSpider(scrapy.Spider):
    name = 'zimu'
    start_urls = [r'http://www.zimuku.cn']

    def parse(self, response):
        """处理start_urls中的链接经下载器返回的response
        """
        for i in xrange(1, 95001):
            url = r'http://www.zimuku.cn/detail/%s.html' % i
            request = scrapy.Request(url=url, callback=self.parse_zimu_detail)
            time.sleep(0.1)
            yield request

    def parse_zimu_detail(self, response):
        """解析内容页
        """
        zimu_url = response.url
        zimu_id = zimu_url.split('/')[-1].split('.')[0]
        zimu_title = response.xpath(
                '//div[@class="md_tt prel"]/h1/text()').extract_first()
        zimu_douban_url = response.xpath(
                '//div[@class="tbhd clearfix"]/ul/li[2]/a/@href').extract_first()
        zimu_language = response.xpath(
                '//ul[@class="subinfo clearfix"]/li[1]/img/@alt').extract()
        zimu_format = response.xpath(
                '//ul[@class="subinfo clearfix"]/li[2]/span/text()').extract()
        zimu_from = response.xpath(
                '//ul[@class="subinfo clearfix"]/li[6]/a/span/text()').extract_first()
        zimu_upload_time = response.xpath(
                '//ul[@class="subinfo clearfix"]/li[7]/text()').extract_first()
        zimu_person = response.xpath(
                '//ul[@class="subinfo clearfix"]/li[7]/a/font/text()').extract_first()
        relative_url = response.xpath(
                '//ul[@class="subinfo clearfix"]/li[10]/div/a/@href').extract_first()
        zimu_download_url = r'http://www.zimuku.cn%s' % relative_url
        zimu_detail_item = ZimuDetailItem(
                zimu_url=zimu_url, zimu_id=zimu_id, zimu_title=zimu_title,
                zimu_douban_url=zimu_douban_url, zimu_language=zimu_language,
                zimu_format=zimu_format, zimu_from=zimu_from,
                zimu_upload_time=zimu_upload_time, zimu_person=zimu_person,
                zimu_download_url=zimu_download_url,
                )
        yield zimu_detail_item
