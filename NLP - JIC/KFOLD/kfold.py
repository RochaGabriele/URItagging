import json
import os
import codecs
import random
import numpy as np
import itertools

actualFolder = os.getcwd()

class K_fold():
    data = []
    k = 0
    nQuestion = 0
    nQuestionsGroup = []
    nPermanentQuestions = []
    permanentQuestionsList = []
    nQuestionGroupBlocks = []
    
    def __init__(self, k):
        self.k = k
    
    def doEveryThing(self):
        self.setVariables()                 #Set initial variables: data, k, nQuestion, nPermanentQuestions
        self.processPermanentQuestions()    #Processar questões permanentes para o número de questões ficar igual
        self.sliceData()                    
        self.joinData()

    def setVariables(self):
        #Data:
        for i in range(8):
            with open(actualFolder + "/Dataset/" + str(i+1) + "data.json", "r") as f:
                self.data.append(json.load(f)) 
        #nQuestion:
        for item in self.data:
            self.nQuestion += len(item)
        #nQuestionsGroup
        for i in range(8):
            self.nQuestionsGroup.append(len(self.data[i]))
        #nPermanentQuestions:
        for i in range(8):
            self.nPermanentQuestions.append(self.nQuestionsGroup[i]%self.k)
            
    def processPermanentQuestions(self):
        #Prepare permanentQuestionsList:
        for i in range(8):
            self.permanentQuestionsList.append([])
        
        #Get n permanent questions:            
        alreadyDrawn = []
        for i, item in enumerate(self.nPermanentQuestions):
            for j in range(item):        
                dataDrawn = random.choice(self.data[i])
                while dataDrawn in alreadyDrawn:
                    dataDrawn = random.choice(self.data[i])
                alreadyDrawn.append(dataDrawn) 
                self.permanentQuestionsList[i].append(dataDrawn)
                self.nQuestionsGroup[i] -= 1
                
        #Remove n permanent questions from data:      
        numberList = []
        for item in self.permanentQuestionsList:
            for j in item:
                numberList.append(j['numero'])
        
        #indexToRemove = 0
        #for i, item in enumerate(permanentQuestionsGroupList):
        for i in range(8):
            self.data[i][:] = [d for d in self.data[i] if d.get("numero") not in numberList]
    
    def sliceData(self):
        slicedData = []
        helpList = []
        
        for i in range(8):
            z = self.nQuestionsGroup[i]/self.k
            self.nQuestionGroupBlocks.append(z)
        
        for i, item in enumerate(self.data):
            newItem = np.array(item)
            slicedItens = np.split(newItem, self.k) 
            for slicedItem in slicedItens:
                backToNormal = slicedItem.reshape(-1,).tolist()
                helpList.append(backToNormal)
            slicedData.append(helpList)
            helpList = []        
        self.data = slicedData

    def joinData(self):
        finalDataSplited = []
        
        trainSet = []
        testSet = []
        returnTrainSet = []
        returnTestSet = []
        
        for group in self.data:
            for question in range(len(group)):    
                trainSet.append(group[:question] + group[question+1:])
                testSet.append(group[question])
            returnTrainSet.append(trainSet)
            returnTestSet.append(testSet)
            trainSet = []   
            testSet = []
                          
        for i in range(8):
            finalDataSplited.append([])
            finalDataSplited[i].append(returnTrainSet[i])
            finalDataSplited[i].append(returnTestSet[i])
        
        #JOIN EVERYBODY
        finalData = []
        helpData = []
        finalTestSet = []
        finalTrainSet = []
        
        for j in range(self.k):
            for i in range(8):
                trainKSet = finalDataSplited[i][0][j]
                testKSet = finalDataSplited[i][1][j]
                           
                for listQuestion in trainKSet:
                    for question in listQuestion:
                        finalTrainSet.append(question)
                for question in testKSet:
                    finalTestSet.append(question)   
            helpData.append(finalTrainSet)
            helpData.append(finalTestSet)
            finalData.append(helpData)
                
            helpData = []
            finalTestSet = []
            finalTrainSet = [] 
            
        self.data = finalData
    
    def giveMeKFold(self, index):
        ###print("------------------------------------")
        ###print("In this K-fold...")
        ###print("We have " + str(self.nQuestion) + " questions in this k-fold")
        ###print("We have n questions in each group:")
        ###print(self.nQuestionsGroup)
        ###print("------------------------------------")
        return self.data[index][0], self.data[index][1]   
    
