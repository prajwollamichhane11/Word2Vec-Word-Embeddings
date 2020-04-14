# -*- coding: utf-8 -*-
import scrapy

class OnlinescraperSpider(scrapy.Spider):
    name = 'onlineScraper'
    allowed_domains = ['www.onlinekhabar.com/content/news']
    start_urls = ['https://www.onlinekhabar.com/content/news/page/95']

    def __init__(self):
        self.newsCount = 0
        self.source = None

    def parse(self, response):
        NewsLinks = response.xpath('//div[@class="item"]/div[@class="item__wrap"]/a/@href').extract()
        NextPage = response.xpath('//a[@class="next page-numbers"]/@href').extract()[0]


        for link in NewsLinks:
            self.newsCount += 1
            print("**********")
            print(self.newsCount)
            print("**********")
            self.source = link
            yield scrapy.Request(self.source,self.parse_article, dont_filter=True)

        if self.newsCount <= 421:
            yield scrapy.Request(NextPage,dont_filter=True)

    def parse_article(self,response):
        title = response.xpath("//div[@class='nws__title--card']/h2/text()").extract()[0]
        article = response.xpath('//div[@class="col colspan3 main__read--content ok18-single-post-content-wrap"]/p/text()').extract()
        NewsLinks = self.source

        article_final = ''.join(article)
        yield{
            # "News Source":NewsLinks,
            # "News Title":title,
            "News Article":article_final
        }
