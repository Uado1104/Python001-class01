# -*- coding: utf-8 -*-
import sys
import uuid
import scrapy
from scrapy.selector import Selector

from crawldatapro.items import CrawldataproItem


class SmzdmspiSpider(scrapy.Spider):
    name = 'smzdmspi'
    allowed_domains = ['smzdm.com']
    start_urls = ['http://smzdm.com/']

    def get_comment_page(self,pstr):
        m = int(pstr)
        m_result = int(0)
        if m == 0:
            pass
        else:
            r_rem = 16 % 30
            r_mod = 16 // 30
            if r_rem > 0:
                r_mod = r_mod + 1
            m_result = r_mod
        return m_result

    # 爬虫启动时，引擎自动调用该方法，并且只会被调用一次，用于生成初始的请求对象（Request）。
    # start_requests()方法读取start_urls列表中的URL并生成Request对象，发送给引擎。
    # 引擎再指挥其他组件向网站服务器发送请求，下载网页
    def start_requests(self):
        for i in range(1, 2):
            url = f'https://www.smzdm.com/fenlei/qipaoshui/p{i}'
            yield scrapy.Request(url=url, callback=self.parse_products)
            # url 请求访问的网址
            # callback 回调函数，引擎回将下载好的页面(Response对象)发给该方法，执行数据解析
            # 这里可以使用callback指定新的函数，不是用parse作为默认的回调参数

    # 解析函数
    def parse_products(self, response):
        # 打印网页的url
        # print(f'开始处理：{response.url}')
        # 打印网页的内容
        # print(response.text)
        bandlist = []
        if response.url == 'https://www.smzdm.com/fenlei/qipaoshui/':
            bands = Selector(response=response).xpath('/html/body/div[1]/div/div[3]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div/a')
            for band in bands:
                m = str(band.xpath('./text()').extract_first()).strip('\n').strip()
                bandlist.append(m)
                # print(m)

        products = Selector(response=response).xpath('//li[@class="feed-row-wide"]')
        if products:
            for product in products:
                title = product.xpath('./div/div[2]/h5/a/text()')
                link = product.xpath('./div/div[2]/h5/a/@href')
                zhi = product.xpath('//div/div[2]/div[4]/div[1]/span/a[1]/span[1]/span/text() | //div/div[2]/div[2]/div[1]/span[1]/span[1]/span[1]/span/text()')
                buzhi = product.xpath('//div/div[2]/div[4]/div[1]/span/a[2]/span[1]/span/text() | //div/div[2]/div[2]/div[1]/span[1]/span[2]/span[1]/span/text()')
                collectcount = product.xpath('//div/div[2]/div[4]/div[1]/a[1]/span/text()')
                commentcount = product.xpath('//div/div[2]/div[4]/div[1]/a[2]/span/text()')
                platform = product.xpath('//div/div[2]/div[4]/div[2]/span/a/text()')
                publish = product.xpath('//div/div[2]/div[4]/div[2]/span/text()')

                productitem = CrawldataproItem()
                productitem['title'] = str(title.extract_first()).strip('\n').strip()
                productitem['link'] = str(link.extract_first()).strip('\n').strip()
                productitem['zhi'] = str(zhi.extract_first()).strip('\n').strip()
                productitem['buzhi'] = str(buzhi.extract_first()).strip('\n').strip()
                productitem['collectcount'] = str(collectcount.extract_first()).strip('\n').strip()
                productitem['commentcount'] = str(commentcount.extract_first()).strip('\n').strip()
                productitem['platform'] = str(platform.extract_first()).strip('\n').strip()
                productitem['publish'] = str(publish.extract_first()).strip('\n').strip()
                productitem['uid'] = str(uuid.uuid1())
                productitem['bands'] = bandlist

                print(f"产品内容：{productitem['title']}-{productitem['link']}-{ productitem['zhi']}-{productitem['buzhi']}-{productitem['collectcount']}-{productitem['commentcount']}-{productitem['platform']}-{productitem['publish']}")

                # 实现评论翻页功能（思路：每页最多30个评论，根据评论数推断评论页数）
                page_count = self.get_comment_page(productitem['commentcount'])
                if page_count > 0:
                    for i in range(1, page_count+1):
                        url = f'{link.extract()[0]}/p{i}'
                        yield scrapy.Request(url=url, meta={'item': productitem}, callback=self.parse_details)
                else:
                    yield productitem

    # 解析具体页面
    def parse_details(self, response):
        print('-----------------------开始评论详情---------------------------------------')
        print(response.url)
        details = Selector(response=response).xpath('//li[@class="comment_list"]')
        productitem = response.meta['item']
        mlist = []
        if details:
            for detail in details:
                publisher = str(detail.xpath('./div[2]/div[1]/a/span/text()').extract_first().strip('\n').strip())
                datePublished = str(detail.xpath('./div[2]/div[1]/div[1]/meta/@content').extract_first().strip('\n').strip())
                timePublished = str(detail.xpath('./div[2]/div[1]/div[1]/text()').extract_first().strip('\n').strip())
                comment = str(detail.xpath('./div[2]/div[3]/div[1]/p/span/text() | ./div[2]/div[2]/div[1]/p/span/text()').extract_first().strip('\n').strip())
                print(f'评论内容：{publisher}-{datePublished}-{timePublished}-{comment}')
                dict = {'uid':productitem['uid'],'publisher':publisher,'datePublished': datePublished,'timePublished':timePublished, 'comment':comment}
                mlist.append(dict)
        productitem['comments'] = mlist
        yield productitem

