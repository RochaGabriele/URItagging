import re

from scrapy.spiders import Spider
from scrapy.selector import Selector

#---------------------------------------------------#
class URISpider(Spider):
    name = "URI"
    
    allowed_domains = ["urionlinejudge.com.br"]
    idNumber = 0
    tagNumber = 0
    tagName = ""
    nivel = []
    
    returnList = []
    
    custom_settings = {
        'DOWNLOAD_HANDLERS' : {'s3': None,}
    }
    
    def __init__(self, *args, **kwargs):
        super(URISpider, self).__init__(*args, **kwargs)
        self.start_urls = kwargs.get("urls")
        
    def parse(self, response):
        sel = Selector(response)
        
        self.idNumber = response.xpath('//tbody/tr/td[1]/a/text()').extract()
        #removeEncodeHelpList = []
        #for items in self.idNumber:
        #    removeEncodeHelpList.append(re.sub(r'[\t\n\r]', '', items).replace(" ", "").encode('utf-8'))
        #self.idNumber = removeEncodeHelpList
        #self.idNumber = [x for x in self.idNumber if x.isdigit()]
        
        #self.tagName = response.xpath('//div[@id="page-name-c"]/h1/text()').extract()[0].encode('utf-8')
        
        HelptagNumber = response.url
        self.tagNumber = list(re.compile(".*index/(.*)\?page.*").match(HelptagNumber).groups())[0]
        
        self.nivel = response.xpath('//td[@class="tiny"]/text()').extract()
        removeEncodeHelpList = []
        for items in self.nivel:
            removeEncodeHelpList.append(re.sub(r'[\t\n\r]', '', items).replace(" ", "").encode('utf-8'))
        self.nivel = removeEncodeHelpList
        self.nivel = [x for x in self.nivel if x]
        
        self.returnList.append(self.idNumber)
        #self.returnList.append(self.tagName)
        self.returnList.append(self.tagNumber)
        self.returnList.append(self.nivel)
        
#---------------------------------------------------#
