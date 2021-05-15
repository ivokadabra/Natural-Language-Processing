import math

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
                    
        l=len(data)
        m=doc_num/len(data)
        k=math.log2(doc_num/len(data))

        d={
           "klasse":c,
            "probability": math.log2(doc_num/len(data))
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
    proba=0
    
    for klasse in C:
        
        for i in data:
            
            if i[0]==klasse:
                
                    #combined_document.append([])
                if i[2] not in conteiner:    
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
            
            p=(counter+1)/(c+V)
            
            proba+=math.log2(p)
            
        d={
           "klasse":klasse,
            "probability":proba
        }    
        
        probability.append(d)
        proba=0
        count+=1
        
    print(probability)
    
    return probability,combined_document


data =[["C1","d1","aab"],["C1","d2","aac"],["C2","d3","ab"],["C2","d4","abb"],["C3","d5","bc"],["C1","d6","aaacc"],["C3","d7","acc"],["C2","d8","abbb"]]

C=["C1","C2","C3"]
𝑉 =["a","b","c"]

con_p,combined_document=con_probability(data,C,len(V))

con_d=count_doc(data,C)

print(con_d)

full_prob=calc_prob(C) 

full_prob