# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
from pathlib import Path

import scrapy
from itemadapter import ItemAdapter
from scrapy.http.request import NO_CALLBACK
from scrapy.utils.defer import maybe_deferred_to_future


class GushiwenPipeline(object):
    content = []

    def __init__(self):
        self.f = None

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

    def __init__(self):
        self.f = None

    def open_spider(self, spider):
        self.f = open(f"assets/data/dump/author.json", 'w')

    def close_spider(self, spider):
        json.dump(self.content, fp=self.f, indent=4)
        self.f.close()

    # https://doc.scrapy.org/en/latest/topics/item-pipeline.html
    async def process_item(self, item, spider):
        # 写入json文件
        item_dict = ItemAdapter(item).asdict()
        self.content.append(item_dict)

        # 下载 image
        # image_url = quote(item_dict['image'])
        image_url = item_dict['image']
        request = scrapy.Request(image_url, callback=NO_CALLBACK, headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
        })
        response = await maybe_deferred_to_future(
            spider.crawler.engine.download(request)
        )
        if response.status != 200:
            # Error happened, return item.
            return item

        file_name = f"{item_dict['name']}.png"
        Path(f"assets/data/dump/authors/{file_name}").write_bytes(response.body)
        return item


class PoetPipline(object):
    content = []

    def __init__(self):
        self.f = None

    def open_spider(self, spider):
        self.f = open(f"assets/data/dump/poet.json", 'w')

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
