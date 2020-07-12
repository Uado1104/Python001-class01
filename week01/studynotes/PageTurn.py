# 需求：获取《豆瓣电影TOP250的内容》
# https://movie.douban.com/top250?start=0
# 获取电影名称、上映日期、评分；写入文本文件
# 引用库
import requests
from bs4 import BeautifulSoup as bs

def get_url_name(myurl):
    user_agent = ' '
    header = {'user-agent':user_agent}
    response = requests.get(myurl,headers = header)
    bs_info = bs(response.text,'html.parser')

    for tags in bs_info.find_all('div', attrs={'class':'hd'}):
        for atag in tags.find_all('a',):
            # 获取所有链接
            print(atag.ger('href'))
            # 获取电影名字
            print(atag.find('span',).text)

    # 生成包含所有页面的元组
    urls = tuple(f'http://movie.douban.com/top250?start={ page * 25 }&filter=' for page in range(10))

    print(urls)
    # 控制请求的频率
    from time import sleep
    sleep(10)
    for page in urls:
        get_url_name(page)
        sleep(5)