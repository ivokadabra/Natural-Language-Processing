
def calssification(C,word_to_class,test_1):
    
    classen_beziehung={}
    
    for test in test_1:
        
           for word in word_to_class:
                
                if test[0]==word['doc']:
                    
                    if (word['klasse'],test[1]) in  classen_beziehung:
                        
                        classen_beziehung[(word['klasse'],test[1])]+=1
                        
                    else:
                        classen_beziehung[(word['klasse'],test[1])]=1
                        
                else:
                    if (word['klasse'],test[1]) in  classen_beziehung:
                        
                        classen_beziehung[(word['klasse'],test[1])]+=0
                        
                    else:
                        classen_beziehung[(word['klasse'],test[1])]=0
                        
     
    print(classen_beziehung)
    
    auswertung_num=0
    auwertung_teiler=0
    auswertung=[]
    num=0
    teiler=0
    num_1=0
    teiler_1=0
    recalls=[]
    precision=[]
    auswertrung=0
    p=0
    t=0
    macro_pressision=0
    
    for klasse in C:
        
        for klasse_1 in C:
            
            if (klasse,klasse_1) in classen_beziehung:
            
                if klasse == klasse_1:
                     num+=classen_beziehung[(klasse,klasse_1)]
                     
                     p+=num
                    
                     auswertung_num+=num
                
                
                teiler+=classen_beziehung[(klasse,klasse_1)] 
                t+=teiler
                auwertung_teiler+=teiler
                    
            if (klasse_1,klasse) in classen_beziehung:
            
                if klasse == klasse_1:
                    num_1+=classen_beziehung[(klasse_1,klasse)]
                        
                    auswertung_num+=num   
                
               
                teiler_1+=classen_beziehung[(klasse_1,klasse)]
                auwertung_teiler+=teiler_1
                    
        auswertung.append({'klasse':klasse,'auswertung':auswertung_num/auwertung_teiler})
        
        
        if teiler==0 or num==0:
            ganz=0
        else:
            ganz=num/teiler
        
        if teiler_1==0 or num_1==0:
            ganz_1=0
        else:
            ganz_1=num_1/teiler_1
            
        recalls.append({'klasse':klasse,'recall':ganz})
        precision.append({'klasse':klasse,'precision':ganz_1})
        
        teiler=0
        num=0
        teiler_1=0
        num_1=0
   
    micro_avg=p/t 
    
    print(p)
    
    print(t)
    
    print(recalls)
    
    print(precision)
    
    print(micro_avg)
    
    macro_avg=0
    
    for i in precision:
        macro_avg+=i['precision']
        
    macro_avg/=len(precision)
    
    print(macro_avg)
    
    print(auswertung)
    
        
        
        
                    
def fin_class(con_p,test,V):
    maximum=0
      
    d={
        "klasse":"",
        "word":""
    }  
        
      
    for i in con_p:
        if test[1] in i['data']:
            count=i['data'].count(test[1])
            length=len(i['data'])
            prob=(count+1)/(length+len(V))
            if maximum< prob:
                maximum=prob
                d={
                    "klasse":i['klasse'],
                    "word": test[1],
                    "doc":test[0]
                }
        else:
            length=len(i['data'])
            prob=1/(length+len(V))
            if maximum< prob:
                maximum=prob
                d={
                    "klasse":i['klasse'],
                    "word": test[1],
                    "doc":test[0]
                }
            
    return  d   


def calc_prob(C):
    
    full_prob=[]

    for klasse in range(len(C)):
    
       d={
        "klasse":con_p[klasse]['klasse'],
        "probability":con_p[klasse]['probability']*con_d[klasse]['probability']
        }
    
       full_prob.append(d)
    
    return full_prob


def count_doc(data,C):
    count_doc=[]
    counter=0
    doc_num=0
    
    for c in C:
        for i in data:
            if i[0]==c:
                 doc_num+=1
                    

        d={
           "klasse":c,
            "probability":doc_num/len(data)
        }
        count_doc.append(d)
        doc_num=0
    return count_doc     
        

def con_probability(data,C,V):
    
    combined_document=[]
    conteiner=[]
    counter=0
    count=0
    probability=[]
    proba=1
    
    for klasse in C:
        
        for i in data:
            
            if i[0]==klasse:
                
                    #combined_document.append([])
                    conteiner.append(i[2])
                    d={
                       "klasse":klasse,
                        "data":conteiner
                    }
                    
                    
                
        combined_document.append(d)       
        counter+=1
        conteiner=[] 
    
    print(combined_document)
          

    for klasse in C:
        c=len(combined_document[count]['data'])
        
        for i in range(c):
            
            word=combined_document[count]['data'][i]
            print(word)
            counter=combined_document[count]['data'].count(word)
            print(counter)
            
            le6ta=(counter+1)/(c+V)

            proba*=(counter+1)/(c+V)
            
        d={
           "klasse":klasse,
            "probability":proba
        }    
        
        probability.append(d)
        proba=1
        count+=1
        
    print(probability)
    
    return probability,combined_document
                
    
    




data =[["C1","d1","aab"],["C1","d2","aac"],["C2","d3","ab"],["C2","d4","abb"],["C3","d5","bc"],["C1","d6","aaacc"],["C3","d7","acc"],["C2","d8","abbb"]]

C=["C1","C2","C3"]
𝑉 =["a","b","c"]
con_p,combined_document=con_probability(data,C,len(V))

con_d=count_doc(data,C)

#print(con_d)

full_prob=calc_prob(C)   

#print(full_prob)

test=[["t1","ab"],["t2","bbbbc"],["t3","abbcd"],["t4","bbcce"],["t5","aac"]]

word_to_class=[]

for i in test:
    word_to_class.append(fin_class(combined_document,i,V))
    
print(word_to_class)


test_1=[["t1","C1"],["t2","C3"],["t3","C2"],["t4","C2"],["t5","C1"]]

calssification(C,word_to_class,test_1)