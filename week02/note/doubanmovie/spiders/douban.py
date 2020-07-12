import scrapy
from bs4 import BeautifulSoup
from week01.spiders.doubanmovie.items import DoubanmovieItem

class DoubanSpider(scrapy.Spider):
    # 定义爬虫名字
    name = 'douban'
    allowed_domains = ['movies.douban.com']
    start_urls = ['http://movie.douban.com/top250']
    # 注释默认的parse函数
    # def parse(self, response):
    #     pass

    # 爬虫启动时，引擎自动调用该方法，且只会调用一次，用于生成初始的请求对象（Request）。
    # start_request()方法读取start_urls列表中的URL并生成Requests对象，发送给引擎。
    # 引擎再指挥其它组件向网站服务器发送请求，下载网页。
    def start_requests(self):
        for i in range(0,10):
            url = f'http://movie.douban.com/top250?start={i*25}'
            yield scrapy.Request(url = url, callback= self.parse)
            # url 请求访问网站
            # callback 回调函数，引擎会将下载好的页面（Response对象）发给该方法，执行数据解析
            # 这里可以使用callback指定新的函数，不是用parse作为默认的回调参数。
    
    # 解析函数
    def parse(self, response):
        # 解藕，通过管道传递到不同的存储介质上
        items = []
        soup = BeautifulSoup(response.text, 'html.parser')
        title_list = soup.find_all('div', attrs={'class':'hd'})
        for i in range(len(title_list)):
            # for i in titile_list
                # 在items.py定义
            item = DoubanmovieItem
            title = title_list[i].find('a').find('span').text
            link = title_list[i].find('a').get('href')
            item['title'] = title
            item['link'] = link
            items.append(item)
        return items