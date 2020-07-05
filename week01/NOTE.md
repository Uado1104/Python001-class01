# 学习笔记--使用Python库获取豆瓣影评
## 用requests简单爬虫
```
# 需求：获取《豆瓣电影TOP250的内容》
# https://movie.douban.com/top250?start=0
# 获取电影名称、上映日期、评分；写入文本文件
# 引用库
import requests
# headers用于requests模拟浏览器
user_agent = ''
header = {'user-agent':user_agent}
# 定义爬取的url
myurl = 'https://movie.douban.com/top250'
#requests.get方法，url传递给requests库
#headers可以使requests库模拟浏览器
response = requests.get(myurl,headers = header)
print(response.text)
# 返回网页的状态码,200代表正常返回
print(f'返回码时：{response.status_code}')
```
## 使用BeautifulSoup解析爬取的网页
```
# 引用库
import requests
# bs4为包，BeautifulSoup为库
from bs4 import BeautifulSoup as bs
# headers用于requests模拟浏览器
user_agent = ''
header = {'user-agent':user_agent}
# 定义爬取的url
myurl = 'https://movie.douban.com/top250'
# requests.get方法，url传递给requests库
# headers可以使requests库模拟浏览器
response = requests.get(myurl,headers = header)
# html为一种解析方式，搜索网页
bs_info = bs(response.text, 'html.parser')

# Python 中使用 for in 形式循环，Python使用缩进来做语句块分隔
# find_all为模拟鼠标动作，加入过滤条件
for tags in bs_info.find_all('div',attrs={'class': 'hd'}):
    for atag in tags.find_all('a',):
        # 获取所有链接
        print(atag.get('href'))
        # 获取电影名字
        print(atag.find('span',).text)
```
