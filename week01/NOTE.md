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
## Scrapy框架结构解析
### 引擎（Engine）
“大脑”，指挥其它组件的协同工作，高效处理并行的请求。<br>
无需修改，框架已写好。
### 调度器（Scheduler）
调度器接收引擎发过来的请求，按照先后顺序，压入队列中，同时去除重复的请求。<br>
无需修改，框架已写好。
### 下载器（Downloader）
相当于requests，下载器用于下载网页内容，并返回给爬虫。<br>
无需修改，框架已写好。
### 爬虫（Spiders）
相当于BeautifulSoup和lxml，用于从特定的网页中提取需要的信息，即所谓的实体（Item）；用户也可以从中提取链接，让Scrapy继续抓取下一个页面。<br>
需要修改。
### 项目管道（Item Piplines）
项目管道负责处理爬虫从网页中抽取的实体，存储数据（csv/txt/MySQL）；主要的功能是持久化实体、验证实体的有效性、清除不需要的信息等。<br>
需要修改
### 下载中间件（Downloader Middlewares）
获取网页-个性化部分<br>
一般不用。
### 爬虫中间件（Spider Middlewares）
获取网页-个性化部分<br>
一般不用。
### 项目流程
引擎——爬虫——调度器——下载中间件——下载器——引擎——爬虫中间件——爬虫——调度器（循环）/项目管道（存储数据）

## Scrapy爬虫目录结构解析
### Scrapy目录结构 
1. spiders目录——实现爬虫的Python文件
2. settings.py——项目的设置文件
3. scrapy.cfg——项目的配置文件
4. items.py——定义所爬取记录的数据结构
5. movies.py——编写爬虫逻辑
6. piplines.py——设置保持位置

### 步骤-mac终端执行
1. ```pip install scrapy```
安装scrapy
2. ```scrapy startproject spiders```spiders为任意项目名称
3. ```cd spiders```
4. ```ls```
<br>显示
scrapy.cfg	spiders
5. ```cd spiders```
6. ```ls```
<br>显示
__init__.py	__pycache__	items.py	middlewares.py	pipelines.py	settings.py	spiders
7. ```ls spiders/```
<br>显示
__init__.py	__pycache__	movies.py
8. ```scrapy genspider movies douban.com``` 
<br>显示
Created spider 'movies' using template 'basic' in module:
	spiders.spiders.movies
9. ```ls```
<br>显示
__init__.py	__pycache__	items.py	middlewares.py	pipelines.py	settings.py	spiders
10. ```ls spiders/```
<br>显示
__init__.py	__pycache__	movies.py
<br>movies.py为我们刚刚使用genspider方式来创建出来的爬虫
###
11. ```cd ../```返回至spiders
12. ```ls```
<br>显示
scrapy.cfg	spiders
13. ```cat scrapy.cfg```
<br>显示
```
[settings]
default = spiders.settings
[deploy]
#url = http://localhost:6800/
project = spiders
```
14. ```cd spiders```
<br>显示
__init__.py	__pycache__	items.py	middlewares.py	pipelines.py	settings.py	spiders
15. ```vim settings.py```
默认的情况下保持不动，当出现异常时进行修改；
vim—— xx 打开xx文件，如果没有就创建xx文件，且跳到编辑页面 
16. ```:q```退出当前
17. ```ls```
<br>显示
__init__.py	__pycache__	items.py	middlewares.py	pipelines.py	settings.py	spiders
18. ```vim spiders```
<br>显示
__init__.py	__pycache__	movies.py
19. ```vim movies.py```打开movies.py设置文件
```
import scrapy
class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['douban.com']
    start_urls = ['http://douban.com/']
    def parse(self, response):
        pass
```
``` allowed_domains = ['douban.com']```限制爬取域名范围在douban.com
``` start_urls = ['http://douban.com/']```第一次请求的url，因为Scrapy运用了twisted的异步请求，只有先去发起一次请求才能启动；另外由于Scrapy在底层写好了一些http的头部信息。
20. ```:q```退出

## yield语句
### yield 和 return 语句
return语句：一次性返回所有的值<br>
yield语句：根据需要，一个值一个值的返回