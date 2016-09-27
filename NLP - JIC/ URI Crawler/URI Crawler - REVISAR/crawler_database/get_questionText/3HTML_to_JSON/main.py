from utils import *

if __name__ == "__main__":
#--------------------------------------------------------------------
#Input: Urls of problems
#Output: JSON File of problems

    #Get problemsFileName and Set JSON File of problems
    json_filename = "database.json"
    
    #List of urls of problems
    problems_urls = get_problems_urls()
    
    #JSON File of problems
    problems_urls = crawl_problems(problems_urls)
    
    #OUTPUT JSON File of lyrics
    output_JSONProblems(json_filename, problems_urls)
#--------------------------------------------------------------------
