import tkFileDialog as filedialog

import os
import codecs
import json

from scrapy.crawler import CrawlerProcess
from spiders import ProblemsSpider

def get_problems_urls():
    filename = filedialog.askopenfilename()
    with open(filename) as f:
        returnList = f.readlines()
    problems_urls = [item.rstrip() for item in returnList]
    return problems_urls    
    
def crawl_problems(urls_array):
    v_spider = ProblemsSpider(urls=urls_array)

    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    process.crawl(v_spider, urls=urls_array)
    process.start()

    return v_spider.problems_array

def output_JSONProblems(json_filename, problems_urls):
    directory = filedialog.askdirectory()
    with codecs.open(os.path.join(directory, json_filename), "w", encoding="utf-8") as fp:
        json.dump(problems_urls, fp, ensure_ascii=False, indent=4, separators=(",", ": "))
