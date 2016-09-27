def dictKmeansToData(data, labelList):
    dic = {0:0, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7}
    #size = []
    for i in range(8):
        indices = [j for j, x in enumerate(labelList) if x == i]   
        #size.append(len(indices))
        topics = []
        for item in indices:
            topics.append(data[item]["assunto"])
        
        mostCommon = mos_common(topics)
        dic[i] = mostCommon
    #print(sorted(size))

    return dic
    
def mos_common(lst):
    return max(set(lst), key=lst.count)
    
