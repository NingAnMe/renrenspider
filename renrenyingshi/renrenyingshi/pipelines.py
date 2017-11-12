# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re
import pymongo
from renrenyingshi.items import RenrenDetailItem

class RenrenPipeline(object):
    def __init__(self, mongo_uri, mongo_db, replicaset):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.replicaset = replicaset

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'renren'),
            replicaset=crawler.settings.get('REPLICASET')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(
            self.mongo_uri, replicaset=self.replicaset)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        if isinstance(item, RenrenDetailItem):
            self._process_renren_detail_item(item)
        else:
            return item

    def _process_renren_detail_item(self, item):
        """处理电影详细信息
        """
        self.db.moviedetail.insert(dict(item))
