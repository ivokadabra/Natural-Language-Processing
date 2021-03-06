import math

def buildTabelle(listOfUnigrams,bigramCounts,unigramCounts):
    matrixX=matrixY=listOfUnigrams
    
    matrixCount=[]
    matrix=[]
   
    for i in range(len(matrixX)):
        
        for j in range(len(matrixY)):
            
            if (matrixX[i],matrixY[j]) in bigramCounts and matrixX[i]!=matrixY[j]:
                
                  #print(matrixX[i],matrixY[j]+ str(bigramCounts[(matrixX[i],matrixY[j])]))
                print(matrixX[i]+str(unigramCounts[matrixX[i]])) 
                      
                number= round(bigramCounts[(matrixX[i],matrixY[j])]/unigramCounts[matrixX[i]],2)  
                matrixCount.append(number)
                
            elif matrixX[i]==matrixY[j] or (matrixX[i],matrixY[j]) not in bigramCounts:
                  #print(matrixX[i],matrixY[j]+ str(0))
                matrixCount.append(0)
                
        matrix.append(matrixCount)
        matrixCount=[]

    print(matrix[0])
    
    
    
    for i in range(len(matrixX)+1):
        
        if (i==0):
            print("#")
        else:
            print(matrixX[i-1],end='')
        
        for j in range(len(matrixY)):
            
            if (i==0):
                print("  "+matrixY[j]+" ",end='')
                
            else: 
                
                
                print("  "+str(matrix[i-1][j])+"  ",end='')
        
                
            
        print('\n')
    
    
    
    
    
    
    return ""
    
    

    
def calcProbability(listOfBigrams, unigramCounts, bigramCounts):
    
    listOfProb = {}
    for bigram in listOfBigrams:
        word1 = bigram[0]
        word2 = bigram[1]
        listOfProb[bigram] = (bigramCounts.get(bigram))/(unigramCounts.get(word1))
    
    return listOfProb
    
    
    

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



def readData(data):
    
    dat=[]
    for i in range(len(data)):
        for word in data[i].split():
            dat.append(word)
    print(dat)
    return dat

def sentenceProb(data_sen,bigramProb):
    
    array_sentences=[]
    sentences=[]
    max_sentence=[]
    
    outputProb1 = 1
    bilist=[]
    for k in range(len(data_sen)):  
      
      splt=data_sen[k].split()
    
      for i in range(len(splt) - 1):
            if(i < len(splt) - 1):

                 bilist.append((splt[i], splt[i + 1]))
     
      for j in bilist:
            if j in bigramProb:
                 outputProb1 *= bigramProb[j]
            else:

                outputProb1 *= 0 
      
      outputProb1=round(outputProb1,2)
      sentences.append((data_sen[k],outputProb1))
      
      if max_sentence==[]:
          max_sentence=sentences

      if sentences[0][1]>max_sentence[0][1]:
            max_sentence=sentences
      
      sentences=[]
    print("The sentence with the biggest probability is:"+ max_sentence[0][0])
    
    return ""

def fortsetzung(word,bigramCounts,listOfBigrams,listOfUnigrams):
    
    probe=[]
    
    for bigram in listOfUnigrams:
        if (word,bigram) in bigramCounts:
           # if bigramCounts[(word,bigram)] > maxBigram
           probe.append((word,bigram,bigramCounts[(word,bigram)]))
    
    print(probe[0][0])
    
    maximum=[0,0,0]
    for i in range(len(probe)):
        if probe[i][2] > maximum[2]:
            maximum=probe[i]
    
    print("The most likely word after "+word+" is "+str(maximum[1]))
    
    #max_value = max(probe[2])

    
    
    return ""


data=['<s> I am Sam </s>',
'<s> Sam I am </s>',
'<s> Sam I like </s>',
'<s> Sam I do like </s>',
'<s> do I like Sam </s>']

data_1=readData(data)

listOfUnigrams,listOfBigrams , bigramCounts, unigramCounts =createBigram(data_1)

#print(listOfBigrams)
print(bigramCounts)
#print(listOfUnigrams)
buildTabelle(listOfUnigrams,bigramCounts,unigramCounts)

bigramProb=calcProbability(listOfBigrams, unigramCounts, bigramCounts)

inputList="<s> I am Sam </s>"
splt=inputList.split()
word=splt[len(splt)-1]

#print(bigramCounts[0])
fortsetzung(word,bigramCounts,listOfBigrams,listOfUnigrams)

data_sen=['<s> I am Sam </s>',
'<s> Sam I do like </s>',
'<s> Sam do I like </s>'
'<s> I do like Sam I am </s>',
'<s> I do like Sam I do like </s>']

sentenceProb(data_sen,bigramProb)


n=5
m=pow(5,1/2)
print(m)
print(math.sqrt(5))