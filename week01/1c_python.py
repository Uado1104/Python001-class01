'''
项目要求：
安装并使用 requests、bs4 库，爬取猫眼电影（）的前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。
'''
# -*- coding: utf-8 -*-
## 使用BeautifulSoup解析网页
import requests
from bs4 import BeautifulSoup as bs
# bs4是第三方库需要使用pip命令安装
import csv

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'

header = {'user-agent':user_agent,
         'Cookie':'__mta=251425081.1593139858651.1593156647624.1593158143829.13; uuid_n_v=v1; uuid=DADDD3F0B75711EAAD7CEBC74F78E0F95A199D6306184D0682B7CFA7C93F750E; _csrf=e3f91413df3e7db171fcb78a33b448d90bad78e4179ac24fe70d618ace08d924; _lxsdk_cuid=172ee890511c8-02e9636521c6b2-31637403-13c680-172ee890512c8; _lxsdk=DADDD3F0B75711EAAD7CEBC74F78E0F95A199D6306184D0682B7CFA7C93F750E; mojo-uuid=d7ae468864ff3ff55d52f747940c6213; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593139858,1593142110; __mta=251425081.1593139858651.1593142110615.1593142228116.8; mojo-session-id={"id":"1a38e36030f97fc123f9d2afb95d1caf","time":1593155873927}; mojo-trace-id=4; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593158143; _lxsdk_s=172ef7d6cbc-cf4-28e-960%7C%7C7'}

myurl = 'https://maoyan.com/films?showType=3'

response = requests.get(myurl,headers=header)

bs_info = bs(response.text, 'html.parser')
# print(bs_info)

list_all=[]
#创建一个列表，用于存储信息
i=0
# 定义爬取电影的数量
top=10

# Python 中使用 for in 形式的循环,Python使用缩进来做语句块分隔
for tags in bs_info.find_all('div', class_='movie-hover-info'):
    i+=1
    if(i<=top):
        # strup = true用于删除空白
        category = tags.get_text(' ',strip=True)
        print(category)
        list = category.split(' ')
        # 'a'模式，追加内容，至于"newline="因为我们的csv文件的类型，防止我们写入东西的时候出现空行。
        csv_1 = open('csv_out.csv','a',newline='')
        outputWriter = csv.writer(csv_1)

        if len(list)==9:
            print(list[0]+'|'+list[4]+'|'+list[8])
            outputWriter.writerow([list[0],list[4],list[8]])
            csv_1.close()
        else:
            print(list[0]+'|'+list[2]+'|'+list[6])
            outputWriter.writerow([list[0],list[2],list[6]])
            csv_1.close()
        print('------------------')
    else:
        break