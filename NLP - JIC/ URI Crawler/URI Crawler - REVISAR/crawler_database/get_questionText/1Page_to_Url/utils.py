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

    return v_spider.problems_array

def output_problems_urls(problems_urls):
    directory = filedialog.askdirectory()
    fileopen = open(os.path.join(directory, "OUTproblems.txt"), "w")
    problems_urls = [str(item) for item in problems_urls]
    problems_urls = ["https://www.urionlinejudge.com.br{0}".format(item) for item in problems_urls]
    
    for item in problems_urls:
        fileopen.write(item + "\n")
        
    return problems_urls
#----------------------------------------------------------------------------------------------------#
