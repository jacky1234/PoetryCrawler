# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

import pymysql


class GushiwenPipeline(object):
    content = []

    def open_spider(self, spider):
        self.f = open("style.origin", 'w')

    def close_spider(self, spider):
        json.dump(self.content, fp=self.f, indent=4)
        self.f.close()

    def process_item(self, item, spider):
        """
        #数据库请用自己的地址替换
        con=MySQLdb.connect(host='xx.xx.xx.xx',user='xx',passwd='xx',db='xx',port=xx,charset='utf8')
        cur=con.cursor()
        cur.execute('insert into Tag values(%s,%s)',("形式",item['style']))
        con.commit()
        con.close()
        print("style",item['style'])
        self.content.append(item)
        """
        return item


class AuthorPipline(object):
    content = []

    def open_spider(self, spider):
        self.f = open("author.json", 'w')

    def close_spider(self, spider):
        json.dump(self.content, fp=self.f, indent=4)
        self.f.close()

    def process_item(self, item, spider):
        # con=MySQLdb.connect(host='xx.xx.xx.xx',user='xx',passwd='xx',db='xx',port=xx,charset='utf8')
        # cur=con.cursor()
        # cur.execute('insert into author values(%s,%s,%s)',(item['name'],item['img'],item['detail']))
        # con.commit()
        # con.close()
        # self.content.append(item)
        return item


class PoetPipline(object):
    content = []

    def __init__(self):
        self.f = None

    def open_spider(self, spider):
        self.f = open(f"assets/poet.origin", 'w')

    def close_spider(self, spider):
        json.dump(self.content, fp=self.f, indent=4)
        self.f.close()

    def process_item(self, item, spider):
        # con = pymysql.connect(host='127.0.0.1', user='test', passwd='test', db='xx', port=3306, charset='utf8')
        # cur = con.cursor()
        # cur.execute('insert into poet values(%s,%s,%s,%s,%s,%s,%s,%s,%s)', (
        #     item['name'], item['dynasty'], item['author'], item['content'], item['tag'], item['fanyi'], item['zhushi'],
        #     item['cankao'], item['shangxi']))
        # con.commit()
        # con.close()
        self.content.append(item)
        print("nNNNNNNNNN", item["n"])
        return item
