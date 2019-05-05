# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import ImagesItem


class PexelsSpider(CrawlSpider):
    name = 'pexels'
    allowed_domains = ['pexels.com']
    start_urls = ['http://pexels.com/']

    rules = (
        Rule(LinkExtractor(allow=r'https://www.pexels.com/photo/.*/$'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = ImagesItem()
        # i['image_urls'] = response.xpath('.//img[@class = "js-photo-page-image-img"]/@src').extract()
        # i['image_urls'] = [response.xpath('.//img[@class = "js-photo-page-image-img"]/@src').extract()]
        i['image_urls'] = response.xpath('.//img[contains(@src,"http")]/@src').extract() # 可以保存但会将杂乱图片下载下来
        return i