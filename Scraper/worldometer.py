import scrapy


class WorldometerSpider(scrapy.Spider):
    name = 'corona'
    
    start_urls = ['https://www.worldometers.info/coronavirus/#countries']

    def parse(self, response):
        for i in range(0 ,215):
            onebyone=response.xpath('//*[@id="main_table_countries_today"]/tbody/tr/td/a[@class="mt_a"]/@href').extract()[i]
            baserul='https://www.worldometers.info/coronavirus/'
            url_country=baserul+onebyone
            yield scrapy.Request(url_country,callback=self.parse_api)


    def parse_api(self,response):
        name=response.css('div>h1::text').extract()[1]
        all_total=response.css('div.maincounter-number>span::text').extract()[0]
        all_deaths=response.css('div.maincounter-number>span::text').extract()[1]
        all_recover=response.css('div.maincounter-number>span::text').extract()[2]
        yield {
                'Country':name,
                'Country Total cases ':all_total,
                'Country Total Deaths ':all_deaths,
                'Country Total Recovered ':all_recover
                }
