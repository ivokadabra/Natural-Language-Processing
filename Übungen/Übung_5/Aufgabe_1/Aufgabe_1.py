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
            prob=count+1/length+len(V)
            if maximum< prob:
                maximum=prob
                d={
                    "klasse":i['klasse'],
                    "word": test[1]
                }
        else:
            length=len(i['data'])
            prob=1/length+len(V)
            if maximum< prob:
                maximum=prob
                d={
                    "klasse":i['klasse'],
                    "word": test[1]
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
            counter=combined_document[count]['data'].count(word)+1
            print(counter)
            
            proba*=counter/(c+V)
            
        d={
           "klasse":klasse,
            "probability":proba
        }    
        
        probability.append(d)
        proba=1
        
    print(probability)
    
    return probability,combined_document
                
    
    




data =[["C1","d1","aab"],["C1","d2","aac"],["C2","d3","ab"],["C2","d4","abb"],["C3","d5","bc"],["C1","d6","aaacc"],["C3","d7","acc"],["C2","d8","abbb"]]

C=["C1","C2","C3"]
V =["a","b","c"]
con_p,combined_document=con_probability(data,C,len(V))

con_d=count_doc(data,C)

full_prob=calc_prob(C)   


test=[["t1","ab"],["t2","bbbbc"],["t3","abbcd"],["t4","bbcce"],["t5","aac"]]

word_to_class=[]

for i in test:
    word_to_class.append(fin_class(combined_document,i,V))
    
word_to_class