import scrapy

class indeedpk(scrapy.Spider):
    name = 'indeed'
    what = input("Enter Job title:")
    where = input("Enter destination:")
    link="https://pk.indeed.com/jobs?q="+what+"&l="+where
    start_urls = [link]

    def parse(self, response):
        
        onebyone='https://pk.indeed.com/viewjob?cmp=ItechX-Ltd&t=SEO+Search+Engine+Optimization+Expert&jk=6dd5bc647576e690&sjdu=CRdQt7s4a9SV5VFAtnE4vGVhFRLiSev_PdckoQeBEChpm9NBsT-eO1wqMUj1DP6CD8tyIatKWL_vt-hfyEheMRu5yxsLfqbghoGejTyyepg&tk=1er49uk1jss13800&adid=361607138&ad=-6NYlbfkN0DpmZqDJx4qfZzfH1pS2S9mIhZDXge-_02zsWaWsNuT-DZPgh_EWKcjlWCh8MnmJZSs3FcM0PUj9GmTJj8kE2ERu8IGDBYg5UHVY-lx6gR8LbZnxpTY73Imrr2giC0Gx-KsuIrdvu2wKIDpqsZmo4rqIr0y1RAmV6HYURTxyWgdfyh90B8i3Z4Hi80HlPtShIDTvrok0rTHsfqFHcUQHAB4XEQY5DejwC1z3TEgGvnu8YRbtATY1r_55xzOJA-H2Z_ot4JUQPGcKU3UgUuo6d_8PBY67tJfV7LqgISOByiCny7bgJ4E5egBIl1FyJ_eF_Bl7mXeg5qWhQ%3D%3D&pub=4a1b367933fd867b19b072952f68dceb&vjs=3'
        url_country=onebyone
        yield scrapy.Request(url_country,callback=self.parse_api)


    def parse_api(self,response):
        job=response.css('div.jobsearch-JobInfoHeader-title-container>h1::text').extract()
        name=response.css('div#jobDescriptionText>ul>li::text').extract()
        
        # all_total=response.css('div.maincounter-number>span::text').extract()[0]
        # all_deaths=response.css('div.maincounter-number>span::text').extract()[1]
        # all_recover=response.css('div.maincounter-number>span::text').extract()[2]
        yield {
                'job':job,
                'Country':name
                
                }
