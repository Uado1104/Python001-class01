# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import os
import csv
import pymysql

conn = pymysql.connect('localhost', 'root', 'mu1995626','Maoyan')
cursor = conn.cursor()
sql1 = """CREATE TABLE movies(
      id int NOT NULL AUTO_INCREMENT,
      名称 val(200) NOT NULL,
      类型 val(50) NOT NULL,
      上映时间 val(100) NOT NULL,
      PRIMARY KET (id))
      ENGINE = MyIASM AUTO_INCREMENT = 1 DEFAULT  CHARSET = utf8mb4"""
cursor.execute(sql1)
class MaoyanPipeline(object):
    def process_item(self, item, spider):
        #return item
        name = item['name']
        tag = item['tag1','tag2','tag3']
        # tag2 = item['tag2']
        # tag3 = item['tag3']
        time = item['time']
        data = [(name, tag, time)]
        sql2 = """
        INSERT INTO TABLE movies(名称, 类型, 上映时间) VALUES  (%s,%s,%s,%s)"""
        try:
            cursor.executemany(sql2, data)
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

        return item

