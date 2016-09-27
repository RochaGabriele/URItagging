import json
import os
import codecs

def joinTwoLists(list1, list2):
    return list1 + list2
    
outputTrainFilename = "trainDatabase.json"
outputTestFilename = "testDatabase.json"

trainFilenames_array = []
for i in range(8):
    trainFileName = str(i+1)+"train_data.json"
    trainFilenames_array.append(trainFileName)
    
testFilenames_array = []
for i in range(8):
    testFileName = str(i+1)+"test_data.json"
    testFilenames_array.append(testFileName)

finalTrainDataList = []
for item in trainFilenames_array:
    with open(item, "r") as f:
        data = json.load(f)
    finalTrainDataList = joinTwoLists(finalTrainDataList, data)

finalTestDataList = []
for item in testFilenames_array:
    with open(item, "r") as f:
        data = json.load(f)
    finalTestDataList = joinTwoLists(finalTestDataList, data)
    
with codecs.open(outputTrainFilename, "w", encoding="utf-8") as fp:
    json.dump(finalTrainDataList, fp, ensure_ascii=False, indent=4, separators=(",", ": "))    

with codecs.open(outputTestFilename, "w", encoding="utf-8") as fp:
    json.dump(finalTestDataList, fp, ensure_ascii=False, indent=4, separators=(",", ": "))
    
