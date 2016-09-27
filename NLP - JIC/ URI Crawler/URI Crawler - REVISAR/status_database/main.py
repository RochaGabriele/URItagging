import json
import os
import codecs


with open("trainDatabase.json", "r") as f:
    trainData = json.load(f)
        
with open("testDatabase.json", "r") as f:
    testData = json.load(f)

numbersInGroupTrain = []
for i in range(8):
    temp = [d for d in trainData if d["assunto"] == str(i+1)]
    numbersInGroupTrain.append(len(temp))

numbersInGroupTest = []
for i in range(8):
    temp = [d for d in testData if d["assunto"] == str(i+1)]
    numbersInGroupTest.append(len(temp))

print(len(trainData))  
print(len(testData))  
print(numbersInGroupTrain)
print(numbersInGroupTest)
