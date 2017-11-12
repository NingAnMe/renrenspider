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
