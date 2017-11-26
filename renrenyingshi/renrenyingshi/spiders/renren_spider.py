# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request

from renrenyingshi.items import RenrenDetailItem

class RenrenSpider(CrawlSpider):
    name = 'renren'
    allowed_domains = ['zimuzu.tv']
    start_urls = ['http://www.zimuzu.tv/resourcelist',]
    rules = (
        Rule(LinkExtractor(
            allow=r'/resourcelist/\?page=\d+&channel=&area=&category=&year=&tvstation=&sort='),
            callback='parse_movie_list', follow=True, process_links='movie_list_url'),
    )

    def parse_movie_list(self, response):
        """解析电影列表页
        """
        movies = response.xpath(
            ".//div[@class='resource-showlist has-point']/ul/li[@class='clearfix']")
        for movie in movies:
            url = movie.xpath(
                "./div[@class='fl-img']/a/@href").extract_first()
            movie_url = r'http://www.zimuzu.tv%s' % url
            movie_id = movie_url.split(r'/')[-1]
            request = scrapy.Request(
                url=movie_url, callback=self.parse_movie_detail)
            request.meta['movie_id'] = movie_id
            yield request

    def parse_movie_detail(self, response):
        """解析电影内容页
        """
        # from scrapy.shell import inspect_response
        # inspect_response(response, self)
        title = response.xpath(
            "//div[@class='resource-tit']/h2/text()").extract_first().strip('"')
        movie_id = response.meta['movie_id']
        movie_url = response.url
        name = response.xpath(
            ".//div[@class='fl-info']/ul/li[1]/strong/text()").extract_first()
        local = response.xpath(
            ".//div[@class='fl-info']/ul/li[2]/strong/text()").extract_first()
        language = response.xpath(
            ".//div[@class='fl-info']/ul/li[3]/strong/text()").extract_first()
        premiere = response.xpath(
            ".//div[@class='fl-info']/ul/li[4]/strong/text()").extract_first()
        company = response.xpath(
            ".//div[@class='fl-info']/ul/li[5]/strong/text()").extract_first()
        if company is None:
            company = u'未知'
        types = response.xpath(
            ".//div[@class='fl-info']/ul/li[6]/strong/text()").extract_first()
        renren_detail_item = RenrenDetailItem(
            title=title, movie_id=movie_id, movie_url=movie_url, name=name,
            local=local,language=language, premiere=premiere, company=company,
            types=types,
        )
        yield renren_detail_item

        def movie_list_url(self, url_list):
            """补全链接地址
            """
            new_url_list = []
            if url_list is None:
                return
            for l in url_list:
                new_url = r'http://www.zimuzu.tv%s' % l
                new_url_list.append(new_url)
            return new_url_list
