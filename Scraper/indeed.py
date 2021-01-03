import scrapy

class indeedpk(scrapy.Spider):
    name = 'indeed'
    what = input("Enter Job title:")
    where = input("Enter destination:")
    link="https://pk.indeed.com/jobs?q="+what+"&l="+where
    start_urls = [link]

    def parse(self, response):
        #onebyone= response.css('h2.title>a::attr(href)')
        onebyone='https://pk.indeed.com/viewjob?cmp=Vaival-Technologies&t=Website+Quality+Assurance&jk=7440a52b7c6594a3&q=html&vjs=3'
        url_country= onebyone
        yield scrapy.Request(url_country,callback=self.parse_api)


    def parse_api(self,response):
        job=response.css('div.jobsearch-JobInfoHeader-title-container>h1::text').extract()
        name=response.css('div#jobDescriptionText>ul>li::text').extract()
        yield {
                'job':job,
                'Country':name
                }
