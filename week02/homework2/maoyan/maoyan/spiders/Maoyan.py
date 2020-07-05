# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from maoyan.items import MaoyanItem

class MaoyanSpider(scrapy.Spider):
    name = 'Maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=2']


    def parse(self, response):
        item = []
        movies = Selector(response=response).xpath('//div[@class="movie-item-hover"]')
        #print(len(movies))
        for movie in movies[0:10]:
            item = MaoyanItem()
            movie_href = movie.xpath('./a/@href').extract_first()
            #print(movie_href)
            yield scrapy.Request(url='https://maoyan.com'+movie_href,meta={'item':item}, callback=self.parse2)


    def parse2(self, response):
        item = response.meta['item']
        try:
            movies_name = Selector(response=response).xpath('//h1[@class="name"]/text()')
            #movies_tag = Selector(response=response).xpath('//h1[@class="name"]/ul/li/a[@class="text-link"]').getall()
            movies_tag1 = Selector(response=response).xpath('//ul/li[1]/a[1][@class="text-link"]/text()').get()
            movies_tag2 = Selector(response=response).xpath('//ul/li[1]/a[2][@class="text-link"]/text()').get()
            movies_tag3 = Selector(response=response).xpath('//ul/li[1]/a[3][@class="text-link"]/text()').get()
            movies_time = Selector(response=response).xpath('//ul/li[3][@class="ellipsis"]/text()').extract_first()
            movies_name = movies_name.extract_first()
            item['name'] = movies_name
            #item['tag'] = movies_tag
            item['tag1'] = movies_tag1
            item['tag2'] = movies_tag2
            item['tag3'] = movies_tag3
            item['time'] = movies_time
            # print(movies_tag1,movies_tag2,movies_tag3)
        except Exception as e:
            print(e)
        finally:
            yield item