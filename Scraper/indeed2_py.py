import scrapy


class Indeed2(scrapy.Spider):
    name = 'indeed2'
    what = input("Enter Job title:")
    where = input("Enter destination:")
    link="https://pk.indeed.com/jobs?q="+what+"&l="+where
    start_urls = [link]
    
    def parse(self, response):
        onebyone= response.css('h2.title>a::attr(href)').extract()
        
        yield {
            'Country':onebyone,
           
        }
