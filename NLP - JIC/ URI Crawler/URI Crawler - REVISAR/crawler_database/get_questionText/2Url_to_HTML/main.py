import tkFileDialog as filedialog
import re

def get_problems_urls():
    filename = filedialog.askopenfilename()
    with open(filename) as f:
        returnList = f.readlines()
    textProblems_urls = [item.rstrip() for item in returnList]
    return textProblems_urls 

def cleanURLS(textProblems_urls):
    listOfNumbers = []
    for item in textProblems_urls:
        number = re.findall(r'[0-9]+$', item)
        listOfNumbers.append(number[0])
    
    openFile = open("textProblems_urls", "w")
    for item in listOfNumbers:
        openFile.write("https://www.urionlinejudge.com.br/repository/UOJ_" + str(item) + ".html\n")
        
textProblems_urls = get_problems_urls()
cleanURLS(textProblems_urls)
