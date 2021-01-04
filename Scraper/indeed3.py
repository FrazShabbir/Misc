import scrapy

class indeedpk(scrapy.Spider):
    name = 'indeed'
    what = input("Enter Job title:")
    where = input("Enter destination:")
    link="https://pk.indeed.com/jobs?q="+what+"&l="+where
    start_urls = [link]

    def parse(self, response):
        links = response.css('div.jobsearch-SerpJobCard')
        for link in  links:
            name = response.css('h2.title::text').get()
            onebyone= link.css('h2.title>a::attr(href)').get()
            baserul='https://pk.indeed.com'
            url_country=baserul+onebyone
            yield scrapy.Request(url_country,callback=self.parse_api)


    def parse_api(self,response):
        job=response.css('div#vjs-desc>ul>li::text').getall()
        job3=response.css('div#jobDescriptionText>ul>li::text').getall()
        job2=response.css('div>p::text').getall()
        
        name = response.css('h1::text').get()

        yield {
            'name':name,
                'job':job,'job3':job3,
                'job2':job2,
                
                }
