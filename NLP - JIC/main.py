
#Author: Hugo Siqueira Gomes

#--------------------------------------
import TFIDF.tfidf as tfidf
import SVD.svd as svd
import KMEANS.kmeans as kmeans
import KFOLD.kfold as kfold

import time
import numpy as np
import helpers as help
#--------------------------------------

#--------------------------------------
#Hyperparameters:
k = 10
k2 = 10
#--------------------------------------

#Read data and separate in K-fold.
kdata = kfold.K_fold(k)
kdata.doEveryThing()


#Para cada k-fold:
for i in range(1):
    
    ###start = time.time()
    
    #Define Train and Test set:
    trainSet, testSet = kdata.giveMeKFold(i)
    
    #Prepare list of documents (sentences)
    corpus = []
    for j in range(len(trainSet)):    
        corpus.append(trainSet[j]["descricao"])
    
    ########### --- PRINT nQuestionsGroup --- ###########
    ###nQuestion = len(trainSet)
    ###nQuestionsGroup = [0,0,0,0,0,0,0,0]
    ###for j in range(len(trainSet)):
    ###    assunto = int(trainSet[j]["assunto"])
    ###    nQuestionsGroup[assunto-1] += 1
        
    ###print("------------------------------------")
    ###print("In this K-fold...")
    ###print("We have " + str(nQuestion) + " questions in this k-fold")
    ###print("We have n questions in each group:")
    ###print(nQuestionsGroup)
    ###print("------------------------------------")
    ########### ----------------------------- ###########
    
    #Calculate Tf-idf vector for train:
    tfIdfmatrix, terms = tfidf.tfIdfMatrix(corpus)
    tfIdfmatrix = np.array(tfIdfmatrix).transpose()

    #Calculate SVD from Tf-idf matrix:
    S, sigma, UT = svd.calculate_svd(tfIdfmatrix, k2)
   
    #Get all doc vectors of trainSet
    doc_vectors = np.dot(sigma, UT).transpose()
    
    #Get kmeans labelList:
    ktrainer = kmeans.kmeans_sklearn(8, doc_vectors)
    labelList = ktrainer.labels_
    
    #####################
    print("--------------")
    for item in labelList[:50]:
        print(item)
    #######################
    
    #Convert to true group in kmeans:
    dicIndex = help.dictKmeansToData(trainSet, labelList)
    newLabelList = []
    for item in labelList:
        newLabelList.append(dicIndex[item])
    print("--------------")
    print(dicIndex)
    print("--------------")
    for item in newLabelList[:50]:
        print(item)
    print("--------------")
        

    
    
    
    
    ###end = time.time()
    ###print(end - start)
