import tkFileDialog as filedialog

import os

from scrapy.crawler import CrawlerProcess
from spiders import URISpider

#----------------------------------------------------------------------------------------------------#
def get_listProblems_urls():
    filename = filedialog.askopenfilename()
    with open(filename) as f:
        returnList = f.readlines()
    problems_urls = [item.rstrip() for item in returnList]
    return problems_urls
    
def crawl_problems(urls_array):
    v_spider = URISpider(urls=urls_array)
    
    process = CrawlerProcess({'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'})

    process.crawl(v_spider, urls=urls_array)
    process.start()

    return v_spider.returnList

def output_classificationTXT(problems_urls):
    directory = filedialog.askdirectory()
    fileopen = open(os.path.join(directory, "classificationTXT.txt"), "w")
    
    
    for j in range(0, len(problems_urls), 3):
        for i, item in enumerate(problems_urls[j]):
            fileopen.write(item + " " + str(problems_urls[j+1]) + " " + str(problems_urls[j+2][i]) + "\n")
#----------------------------------------------------------------------------------------------------#
