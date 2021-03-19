import scrapy


class Indeed2(scrapy.Spider):
    name = 'indeed2'
    what = input("Enter Job title:")
    where = input("Enter destination:")
    link="https://pk.indeed.com/jobs?q="+what+"&l="+where
    start_urls = [link]
    
    def parse(self, response):
        for i in range (1,10):
            name = response.css('h2.title::text').get()
            onebyone= response.css('h2.title>a::attr(href)').get()
            baserul='https://pk.indeed.com'
            url_country=baserul+onebyone[]
            job=response.css('div#vjs-desc>ul>li::text').getall()
            yield {
                'Country':job,
                'name':name
            
            }
