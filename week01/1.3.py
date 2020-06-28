# 需求：获取《豆瓣电影TOP250的内容》
# https://movie.douban.com/top250?start=0
# 获取电影名称、上映日期、评分；写入文本文件
# 引用库
import requests
import lxml.etree
# 爬取页面详细信息
# 电影详细页面
url = 'https://movie.douban.com/subject/1292052/'

user_agent = ''
# 声明为字典使用字典的语法赋值
header = {}
header['user-agent'] = user_agent
response =  requests.get(url,headers = header)
# xml化处理
selector = lxml.etree.HTML(response.text)
# 电影名称
film_name = selector.xpath('//*[@id="content"]/h1/span[1]/text()')
print(f'电影名称：{film_name}')
# 上映日期
plan_data = selector.xpath('//*[@id="info"]/span[10]/text()')
print(f'上映日期：{plan_data}')
# 评分
rating = selector.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')
print(f'评分：{rating}')

mylist = [film_name,plan_data,rating]

import pandas as pd

movie1 = pd.DataFrame(data = mylist)

# windows需要gbk字符集
movie1.to_csv('./movie1.csv',encoding='utf8',index=False,header=False)