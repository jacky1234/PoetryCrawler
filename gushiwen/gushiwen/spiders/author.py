# -*- coding: utf-8 -*-

import scrapy
from scrapy import Item, Field


class AuthorItem(Item):
    name = Field()
    image = Field()
    detail = Field()


# 服务器压力，只能爬到第10页数据
class AuthorSpider(scrapy.Spider):
    name = 'author'
    # allowed_domains = ['https://so.gushiwen.org/authors']
    start_urls = ['https://so.gushiwen.cn/authors/']

    def parse(self, response, **kwargs):
        nextpage = response.css("form .pagesright .amore").css("a::attr(href)").extract()

        for e_cont in response.xpath("//div[@class='sonspic']/div[@class='cont']"):
            author_image = e_cont.css("div[class=divimg] img::attr(src)").get()
            author_name = e_cont.css("p b::text").get()
            author_detail = e_cont.css("p::text").getall()[4]

            author_item = AuthorItem()
            author_item['name'] = author_name
            author_item['image'] = author_image
            author_item['detail'] = author_detail
            yield author_item

            # authorDict.append(
            #     {
            #         'name': author_name,
            #         'img': author_image,
            #         'detail': author_detail
            #     }
            # )

        # if nextpage:
        #     url = "https://so.gushiwen.org" + nextpage[0]
        #     # print("URLLLLLLLLLLL",url)
        #     yield scrapy.Request(url, callback=self.parse)
