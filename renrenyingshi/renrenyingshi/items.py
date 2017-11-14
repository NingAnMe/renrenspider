# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RenrenDetailItem(scrapy.Item):
    # ID
    movie_id = scrapy.Field()
    # 链接
    movie_url = scrapy.Field()
    # 标题
    title = scrapy.Field()
    # 原名
    name = scrapy.Field()
    # 地区
    local = scrapy.Field()
    # 语言
    language = scrapy.Field()
    # 首播时间
    premiere = scrapy.Field()
    # 制作公司
    company = scrapy.Field()
    # 类型
    types = scrapy.Field()

class ZimuDetailItem(scrapy.Item):
    # 链接
    zimu_url = scrapy.Field()
    # ID
    zimu_id = scrapy.Field()
    # 标题
    zimu_title = scrapy.Field()
    # 豆瓣
    zimu_douban_url = scrapy.Field()
    # 语言
    zimu_language = scrapy.Field()
    # 字幕格式
    zimu_format = scrapy.Field()
    # 字幕来源
    zimu_from = scrapy.Field()
    # 上传时间
    zimu_upload_time = scrapy.Field()
    # 制作人
    zimu_person = scrapy.Field()
    # 下载链接
    zimu_download_url = scrapy.Field()
