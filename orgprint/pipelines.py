# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs

class JsonWithEncodingPipeline(object):

    def __init__(self):
        self.file = codecs.open('supplies.json', 'w', encoding='utf-8')
        self.file.seek(0)
        self.file.truncate()

    # def process_item(self, item, spider):
    #     #line = json.dumps(dict(item), ensure_ascii = False, indent = 2) + "\n"
    #     #self.file.write(line)
    #     return item

    def spider_closed(self, spider):
        self.file.close()