# -*- coding: utf-8 -*-
import re
import pandas as pd
import lxml.etree
from bs4 import BeautifulSoup as bs
import requests
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
# 使用BeautifulSoup解析网页
header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "close",
    "Cookie": "_gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1",
    "Referer": "http://httpbin.org/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"
}
myurl = 'https://maoyan.com/films?showType=3'
response = requests.get(myurl, headers=header)
bs_info = bs(response.text, 'html.parser')
# Python 中使用 for in 形式的循环,Python使用缩进来做语句块分隔
urls = []
film_name = []
plan_date = []
film_types = []
for tags in bs_info.find_all('div', attrs={'class': 'channel-detail movie-item-title'}):
    for atag in tags.find_all('a', ):
        # 获取所有链接
        url = 'https://maoyan.com' + atag.get('href')
        urls.append(url)


def get_url_name(furl):
    header = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, sdch",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Connection": "close",
        "Cookie": "_gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1",
        "Referer": "http://httpbin.org/",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"
    }
    response = requests.get(furl, headers=header)
    # xml化处理
    selector = lxml.etree.HTML(response.text)
    # 电影名称
    global film_name
    film = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/h1/text()')
    film_name.append(film[0])
    # 上映日期
    global plan_date
    release_date = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[3]/text()')
    release_date_update = re.sub(r'[^\d-]', "", release_date[0])
    plan_date.append(release_date_update)
    # 电影类型
    global film_types
    Movie_Type = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1]/*/text()')
    film_types.append(','.join(Movie_Type))


for i in urls[0:10]:
    get_url_name(i)

mylist = {}
mylist = {'电影名称': film_name, '上映日期': plan_date, '电影类型': film_types}
movie = pd.DataFrame(data=mylist)
movie.to_csv('./movie.csv', encoding='utf8', index=False, header=False)