def sentenceProplexity(data_sen,bigramProb):
    
    array_sentences=[]
    sentences=[]
    max_sentence=[]
    
    outputProb1 = 1
    bilist=[]
    for k in range(len(data_sen)):  
    
        splt=data_sen[k].split()
        N=len(splt)
            
        for i in range(len(splt) - 1):
            if(i < len(splt) - 1):

                 bilist.append((splt[i], splt[i + 1]))
     
        for j in bilist:
            if j in bigramProb:
                 outputProb1 *= bigramProb[j]
            else:

                outputProb1 *= 0 
      
        #outputProb1=round(outputProb1,3)
        outputProb1=pow(outputProb1,1/N)
        print("The proplexity of sentence"+data_sen[k]+" is:"+str(outputProb1))
    
    return ""




def calcProbability(listOfBigrams, unigramCounts, bigramCounts):
    
    listOfProb = {}
    for bigram in listOfBigrams:
        word1 = bigram[0]
        word2 = bigram[1]
        listOfProb[bigram] = (bigramCounts.get(bigram))/(unigramCounts.get(word1))
    
    return listOfProb



def readData(data):
    
    dat=[]
    for i in range(len(data)):
        for word in data[i].split():
            dat.append(word)
   
    return dat



def createBigram(data):
    listOfBigrams = []
    bigramCounts = {}
    listOfUnigrams = []
    unigramCounts = {}
    for i in range(len(data)-1):
        if i< len(data)-1:
                listOfBigrams.append((data[i],data[i+1]))
                if data[i] not in listOfUnigrams or i==0:
                    listOfUnigrams.append(data[i])
                    
                    
                
                if (data[i],data[i+1]) in bigramCounts:
                        bigramCounts[(data[i],data[i+1])]+=1;
                        
                else:
                    bigramCounts[(data[i],data[i+1])]=1;
                    
                    
        if data[i] in unigramCounts:
             unigramCounts[data[i]] += 1
        else:
            unigramCounts[data[i]] = 1          
                    
    return listOfUnigrams, listOfBigrams , bigramCounts ,unigramCounts 



data=['<s> I am Sam </s>',
'<s> Sam I do like </s>',
'<s> Sam do I like </s>',
'<s> I do like Sam I am </s>',
'<s> I do like Sam I do like </s>']

data_1=readData(data)

listOfUnigrams,listOfBigrams , bigramCounts, unigramCounts =createBigram(data_1)

bigramProb=calcProbability(listOfBigrams, unigramCounts, bigramCounts)
print(bigramProb)

proplexity=sentenceProplexity(data,bigramProb)