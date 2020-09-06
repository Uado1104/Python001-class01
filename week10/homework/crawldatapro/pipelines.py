# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import uuid
import re
import datetime

class CrawldataproPipeline:
    def get_product_publishtime(self,publishstr):
        publishtime = ""
        if '小时' in publishstr:
            mdelta = int(re.findall("\d+", publishstr)[0])
            publishtime = (datetime.datetime.now() + datetime.timedelta(hours=-mdelta)).strftime("%Y-%m-%d %H:%M:%S")
        else:
            publishtime = '2020-' + publishstr + ':00'
        return publishtime

    def get_band_list(self,bands):
        band_values = []
        for band in bands:
            uid = str(uuid.uuid1())
            bandstr = str(band)
            if '/' in bandstr:
                mlist = bandstr.split('/', 1)
                band_english = mlist[0]
                band_chinese = mlist[1]
                band_values.append((uid, bandstr, band_english, band_chinese))
            else:
                band_values.append((uid, bandstr, '', bandstr))
        return band_values

    def get_comment_list(self,commentstr):
        comment_values = []
        for comm in commentstr:
            commenttime = ""
            if '小时' in comm['timePublished']:
                mdelta = int(re.findall("\d+", comm['timePublished'])[0])
                commenttime = (datetime.datetime.now() + datetime.timedelta(hours=-mdelta)).strftime(
                    "%Y-%m-%d %H:%M:%S")
            else:
                # date
                mdate = ""
                mdate_result = re.search(r"(\d{4}-\d{1,2}-\d{1,2})", comm['datePublished'])
                if mdate_result:
                    mdate = mdate_result.group(0)
                # time
                mtime = ""
                mtime_full_result = re.search(r"(\d{1,2}:\d{1,2}:\d{1,2})", comm['timePublished'])
                if mtime_full_result:
                    mtime = mtime_full_result.group(0)
                else:
                    mtime_part_result = re.search(r"(\d{1,2}:\d{1,2})", comm['timePublished'])
                    if mtime_part_result:
                        mtime = mtime_part_result.group(0) + ':00'
                commenttime = mdate + " " + mtime
            comment_values.append((comm['uid'], comm['publisher'], commenttime, comm['comment']))
        return comment_values

    def process_item(self, item, spider):
        print('-----------------------开始Pipeline---------------------------------------')
        uid = item['uid']
        title = item['title']
        link = item['link']
        zhi = item['zhi']
        buzhi = item['buzhi']
        collectcount = item['collectcount']
        commentcount = item['commentcount']
        platform = item['platform']
        publish = item['publish']
        bands = item['bands']
        comments = item['comments']

        # 处理产品的录入时间
        publishtime = self.get_product_publishtime(publish)
        # 获取品牌信息列表
        band_values = self.get_band_list(bands)
        # 获得产品信息对象
        product_values = []
        # product_values = [(uid, title, link, zhi, buzhi, collectcount, commentcount, platform, publishtime)]
        # 获得评论信息列表
        comment_values = []
        # comment_values = self.get_comment_list(comments)

        try:
            conn = pymysql.connect(host='localhost',
                                   port=3306,
                                   user='root',
                                   password='000000',
                                   database='test',
                                   charset='utf8mb4'
                                   )
            # 获得cursor游标对象
            con_cursor = conn.cursor()

            # 执行插入品牌数据
            con_cursor.execute('select *  from zdm_band limit 5;')
            results = con_cursor.fetchall()
            if len(results) != 5 and band_values:
                con_cursor.executemany('INSERT INTO ' + 'zdm_band' + ' values(%s,%s,%s,%s)', band_values)

            # 执行插入产品数据
            if product_values:
                con_cursor.executemany('INSERT INTO ' + 'zdm_product' + ' values(%s,%s,%s,%s,%s,%s,%s,%s,%s)', product_values)

            # 执行插入评论数据
            if comment_values:
                con_cursor.executemany('INSERT INTO ' + 'zdm_comment' + ' values(%s,%s,%s,%s)', comment_values)

            conn.commit()
            con_cursor.close()
            conn.close()
        except Exception as e:
            print(e)  # 输出异常信息