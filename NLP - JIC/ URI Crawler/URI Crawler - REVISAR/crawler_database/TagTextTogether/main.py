import json
import os
import codecs

#Find dictionary's index position:
def find_index(lst, key, value):
    for i, d in enumerate(lst):
        if d[key] == value:
            return i

tagFileName = "TAG8group.txt"
databaseFilename = "8database.json"
outputFilename = "8data.json"

#Pega lista de numero, assunto e nivel
lines = [line.rstrip("\n") for line in open(tagFileName)]
linesList = []
for item in lines:
    a = item.split()
    linesList.append(a)

with open(databaseFilename, "r") as f:
    data = json.load(f)
    

for item in linesList:
    index = find_index(data, "numero", item[0])
    data[index]["assunto"] = item[1]
    data[index]["nivel"] = item[2]
 
with codecs.open(outputFilename, "w", encoding="utf-8") as fp:
    json.dump(data, fp, ensure_ascii=False, indent=4, separators=(",", ": "))
    
