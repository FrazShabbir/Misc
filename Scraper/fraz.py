import scrapy


class frazSpider(scrapy.Spider):
    name = 'fraz'
    
    what = input("Enter Job title:")
    where = input("Enter destination:")
    link="https://pk.indeed.com/jobs?q="+what+"&l="+where
    start_urls = [link]

    def parse(self, response):
        abc =response.css('.jobsearch-SerpJobCard')
        for links in abc:    
            onebyone=links.css('h2.title>a::attr(href)').getall() 
            baserul='https://pk.indeed.com'
            url_country=baserul+onebyone
            yield scrapy.Request(url_country,callback=self.parse_api)


    def parse_api(self,response):
        name=response.css('div#vjs-desc>ul>li::text').getall()
        
        yield {
                'Country':name,
                }
