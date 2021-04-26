import nltk



def sentenceProplexity(data_sen,bigramProb):
    
    text_Proplexity=0
    array_sentences=[]
    sentences=[]
    max_sentence=[]
    n=0
    outputProb1 = 1
    bilist=[]
    for k in range(len(data_sen)):  
    
        splt=data_sen[k]
        N=len(data_sen)
            
        for i in range(len(splt) - 1):
            if(i < len(splt) - 1):

                 bilist.append((splt[i], splt[i + 1]))
     
        for j in bilist:
            
            if j in bigramProb:
                 outputProb1 *= bigramProb[j]
            else:

                outputProb1 *= 1 
      
        #outputProb1=round(outputProb1,3)
        outputProb1=pow(1/outputProb1,1/N)
        #print("The proplexity of sentence"+" is:"+str(outputProb1))
        text_Proplexity+=outputProb1
    
    
    print("The proplexity of the text "+" is:"+str(text_Proplexity))
    
    return ""



def ersetzen(data,listOfUnigrams):
    for i in data:
            for j in i:
                if j not in listOfUnigrams:
                    number=i.index(j)
                    i[number]="<UNK>"
    
    return data 


def fortsetzung(word,bigramCounts,listOfBigrams,listOfUnigrams):
    
    probe=[]
    
    for bigram in listOfUnigrams:
        if (word,bigram) in bigramCounts:
           # if bigramCounts[(word,bigram)] > maxBigram
           probe.append((word,bigram,bigramCounts[(word,bigram)]))
    
    #print(probe[0][0])
    
    maximum=[0,0,0]
    for i in range(len(probe)):
        if probe[i][2] > maximum[2]:
            maximum=probe[i]
    
    print("The most likely word after "+word+" is "+str(maximum[1]))
    
    #max_value = max(probe[2])

    
    
    return ""

def calcProbability(listOfBigrams, unigramCounts, bigramCounts,operator):
    
    listOfProb = {}
    V=len(unigramCounts)
    
    for bigram in listOfBigrams:
        word1 = bigram[0]
        word2 = bigram[1]
        if(operator==False):
             listOfProb[bigram] = (bigramCounts.get(bigram))/(unigramCounts.get(word1))
        else:
             listOfProb[bigram] = (bigramCounts.get(bigram))+1/(unigramCounts.get(word1)+V)
    
    return listOfProb


def calcProbabilitytrigram(listOfTrigrams, unigramCounts, trigramsCount,operator):
    
    listOfProb = {}
    V=len(unigramCounts)
    for trigram in listOfTrigrams:
        word1 = trigram[0]
        word2 = trigram[1]
        word3 = trigram[2]
        if(operator==False):
             listOfProb[trigram] = (trigramsCount.get(trigram))/(unigramCounts.get(word1))
        
        else:
             listOfProb[trigram] = (trigramsCount.get(trigram))+1/(unigramCounts.get(word1)+V)
    
    return listOfProb



def createBigram(data):
    listOfBigrams = []
    bigramCounts = {}
    listOfUnigrams = []
    unigramCounts = {}
    listOfTrigrams=[]
    trigramsCount={}
    
    for i in range(len(data)-1):
        if i< len(data)-1:
                listOfBigrams.append((data[i],data[i+1]))
                
                if data[i] not in listOfUnigrams or i==0:
                    listOfUnigrams.append(data[i])
                    
                    
                
                if (data[i],data[i+1]) in bigramCounts:
                        bigramCounts[(data[i],data[i+1])]+=1;
                        
                else:
                    bigramCounts[(data[i],data[i+1])]=1;
                    
               
                
        if i< len(data)-2:
            
                listOfTrigrams.append((data[i],data[i+1],data[i+2]))
                
                if (data[i],data[i+1],data[i+2]) in trigramsCount:
                        trigramsCount[(data[i],data[i+1],data[i+2])]+=1;
                        
                else:
                    trigramsCount[(data[i],data[i+1],data[i+2])]=1;
                    
        if data[i] in unigramCounts:
             unigramCounts[data[i]] += 1
        else:
            unigramCounts[data[i]] = 1          
                    
    return listOfUnigrams, listOfBigrams , bigramCounts ,unigramCounts,listOfTrigrams,trigramsCount



def tokens(sentence,counter,token_sentences,tokens_for_bigrams):
    p=token_sentences
    if ("<s>" not in p[counter]):
        p[counter].append("<s>")
        tokens_for_bigrams.append("<s>")
    
    for x in nltk.word_tokenize(sentence):

        p[counter].append(x.lower())
        tokens_for_bigrams.append(x)
        if (x=="." or x=="?" or x=="!" or x==";"):
            p[counter].append("<\s>")
            counter+=1
            p.append([])
            p[counter].append("<s>")
   
    #index_1=nltk.word_tokenize(sentence).index("."or"!")
    #index_2=nltk.word_tokenize(sentence).index("!")
    #index_3=nltk.word_tokenize(sentence).index("?")
    #index_4=nltk.word_tokenize(sentence).index(";")
    #p.append(nltk.word_tokenize(sentence))
   
    return p,counter,tokens_for_bigrams



f = open("tales/Hänsel und Gretel.txt", "r")
counter=0
token_sentences=[[]]
tokens_for_bigrams=[]
for x in f:
    
    token_sentences,counter,tokens_for_bigrams=tokens(x,counter,token_sentences,tokens_for_bigrams)
    
f.close()
#print(token_sentences)
#print(tokens_for_bigrams)
listOfUnigrams=[]
listOfBigrams=[] 
bigramCounts={} 
unigramCounts={} 
listOfTrigrams=[]
trigramsCount={}
operator=True
listOfUnigrams, listOfBigrams , bigramCounts ,unigramCounts,listOfTrigrams,trigramsCount=createBigram(tokens_for_bigrams)

bigramProb=calcProbability(listOfBigrams, unigramCounts, bigramCounts,operator=False)
trigramProb=calcProbabilitytrigram(listOfTrigrams, unigramCounts, trigramsCount,operator=False)
bigramProb_laplace=calcProbability(listOfBigrams, unigramCounts, bigramCounts,operator=True)
trigramProb_laplace=calcProbabilitytrigram(listOfTrigrams, unigramCounts, trigramsCount,operator=True)




inputList="<s> es war"
splt=inputList.split()
word=splt[len(splt)-1]

#print(bigramCounts[0])
fortsetzung(word,bigramCounts,listOfBigrams,listOfUnigrams)

text = open("text_1.txt", "r")

counter_1=0
token_sentences_1=[[]]
tokens_for_bigrams_1=[]
for k in text:
    
    token_sentences_1,counter_1,tokens_for_bigrams_1=tokens(k,counter_1,token_sentences_1,tokens_for_bigrams_1)
    #print(k)
    #print(token_sentences_1)
    
data_1=ersetzen(token_sentences_1,listOfUnigrams)
text.close()
sentenceProplexity(data_1,bigramProb_laplace)



text_1= open("text_2.txt", "r")

counter_2=0
token_sentences_2=[[]]
tokens_for_bigrams_2=[]
for k in text_1:
    
    token_sentences_2,counter_2,tokens_for_bigrams_2=tokens(k,counter_2,token_sentences_2,tokens_for_bigrams_2)
    #print(k)
    #print(token_sentences_1)
    
data_2=ersetzen(token_sentences_2,listOfUnigrams)

text_1.close()
sentenceProplexity(data_2,bigramProb_laplace)


#listOfUnigrams_1=[]
#listOfBigrams_1=[] 
#bigramCounts_1={} 
#unigramCounts_1={} 
#listOfTrigrams_1=[]
#trigramsCount_1={}

#listOfUnigrams_1, listOfBigrams_1 , bigramCounts_1 ,unigramCounts_1,listOfTrigrams_1,trigramsCount_1=createBigram(tokens_for_bigrams)

#bigramProb_1=calcProbability(listOfBigrams_1, unigramCounts_1, bigramCounts_1,operator=False)
#trigramProb_1=calcProbabilitytrigram(listOfTrigrams_1, unigramCounts_1, trigramsCount_1,operator=False)


