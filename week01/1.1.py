# 需求：获取《豆瓣电影TOP250的内容》
# https://movie.douban.com/top250?start=0
# 获取电影名称、上映日期、评分；写入文本文件
import requests
myurl = 'https://movie.douban.com/top250'
# headers用于requests模拟浏览器
res = requests.get(myurl)
type(res)
res.status_code == requests.codes.ok
print(res.text[:250])
# 返回网页的状态码
print(f'返回码时：{res.status_code}')