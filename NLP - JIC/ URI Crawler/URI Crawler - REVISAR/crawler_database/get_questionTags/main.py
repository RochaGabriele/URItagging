from utils import *

if __name__ == "__main__":
#--------------------------------------------------------------------
#Input: Urls of URI problems list
#Output: Urls of each problem
       
    #List of urls of URI problems list
    listProblems_urls = get_listProblems_urls()
    
    #List of urls of musics
    problems_urls = crawl_problems(listProblems_urls)
    
    #OUTPUT music_urls
    output_classificationTXT(problems_urls)
#--------------------------------------------------------------------
