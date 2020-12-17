import scrapy


class DarazSpider(scrapy.Spider):
    name = 'daraz'
    start_urls = ['https://www.youtube.com/feed/trending']

    def parse(self, response):
        name=response.xpath('//*[@id="video-title"]/yt-formatted-string/@href/text()').extract()
        yield{
            'name':name
        }
