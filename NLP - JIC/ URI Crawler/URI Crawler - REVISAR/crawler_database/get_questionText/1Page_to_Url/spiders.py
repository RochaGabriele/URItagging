from scrapy.spiders import Spider
from scrapy.selector import Selector

#---------------------------------------------------#
class URISpider(Spider):
    name = "URI"
    
    allowed_domains = ["urionlinejudge.com.br"]
    problems_array = []
    
    custom_settings = {
        'DOWNLOAD_HANDLERS' : {'s3': None,}
    }
    
    def __init__(self, *args, **kwargs):
        super(URISpider, self).__init__(*args, **kwargs)
        self.start_urls = kwargs.get("urls")
        
    def parse(self, response):
        sel = Selector(response)
        links = response.xpath('//td[@class="large"]/a/@href').extract()
        
        for sentence in links:
            self.problems_array.append(sentence)
            
#---------------------------------------------------#
