import scrapy


class CoronaSpider(scrapy.Spider):
    name = 'corona'
    
    start_urls = ['https://www.worldometers.info/coronavirus/country/pakistan/']

    def parse(self, response):
        #data=response.css('.c5TXIP')
        name=response.css('div>h1::text').extract()[1]
        Pakistan_total=response.css('div.maincounter-number>span::text').extract()[0]
        Pakistan_deaths=response.css('div.maincounter-number>span::text').extract()[1]
        Pakistan_recover=response.css('div.maincounter-number>span::text').extract()[2]
        yield {
            'Country':name,
            'Pakistan Total cases ':Pakistan_total,
            'Pakistan Total Deaths ':Pakistan_deaths,
            'Pakistan Total Recovered ':Pakistan_recover
        }
