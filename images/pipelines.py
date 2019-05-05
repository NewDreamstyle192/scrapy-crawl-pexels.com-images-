# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ImagesPipeline(object):
    def process_item(self, item, spider):
        tmp = item['image_urls']
        item['image_urls'] = []
        for i in tmp:
            if 'photos' in i:
                if '?' in i:
                    item['image_urls'].append(i.split('?')[0])
        return item
