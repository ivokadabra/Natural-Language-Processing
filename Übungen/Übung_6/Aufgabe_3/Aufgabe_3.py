import pandas as pd
import math


def LCE(p):
    LCE=[]
    for row_num in range(number_of_rows):
        if p[row_num]['class']=='Iris-setosa':
            y=1
            
        else:
            y=0
        
        upper=p[row_num]['probability']
        down=0
        for row_num1 in range(number_of_rows):
            
            if row_num!=row_num1:
                down+=p[row_num1]['probability'] 
        
        if y==0:
            lce=0
            
        else: 
            
            o=upper/down 
            print(o)
            proba=-y*math.log2(o)
            lce=round(proba,2)
            print(lce)
        
        LCE.append({'class': p[row_num]['class'],'doc_num':row_num,'LCE':lce})
     
    return LCE
              

def calc_z(x,w1,w2,w3,b1,b2,b3):
    
    z_vektor=[]
    #Z={}
    
    for row_num in range(number_of_rows):
            wx=0
            z=0

            p=x[row_num]
            if x[row_num][4]=='Iris-setosa':
                b=b1;
                w=w1
                
            elif x[row_num][4]=='Iris-versicolor':
                b=b2;
                w=w2 
                
            elif x[row_num][4]=='Iris-virginica':
                b=b3;
                w=w3
            
            Class=x[row_num][4]
            
            for i in range(4):
                
                wx+=w[i]*x[row_num][i]
                
            
            z=wx+b
            
            Z={
             'z': round(z,3),
             'class':Class,
             'doc_num':row_num
            }
            z_vektor.append(Z)
                
    return z_vektor                
    
    
    

def probability_datensatz(z):
    
    propbability=[]
    
    for row_num in range(number_of_rows):
        upper=z[row_num]['z']
        down=0
        for row_num1 in range(number_of_rows):
            if row_num != row_num1:
                down+=z[row_num1]['z']
        
        p=upper/down
        
        propbability.append({'probability':round(p,3),'class':z[row_num]['class']})
        
    
    return propbability


x=[]
w1=[1,1,1,1]
w2=[-1,-1,-1,-1]
w3=[2,2,2,2]
b1=1
b2=-1
b3=2
print("TRAINING")
df=pd.read_csv('iris-training.csv')

#print(df.loc[0])
index = df.index
number_of_rows = len(index)

#print(number_of_rows)


for row_num in range(number_of_rows):
        x.append([])
        x[row_num].append(df.loc[row_num]['sepal_length'])
        x[row_num].append(df.loc[row_num]['sepal_width'])
        x[row_num].append(df.loc[row_num]['petal_length'])
        x[row_num].append(df.loc[row_num]['petal_width'])
        x[row_num].append(df.loc[row_num]['species'])

        
        
z=calc_z(x,w1,w2,w3,b1,b2,b3)        
p=probability_datensatz(z)
print(p)
lce=LCE(p)
print(lce)
print("TEST")
x=[]
df=pd.read_csv('iris-test.csv')

index1 = df.index
number_of_rows = len(index1)
for row_num in range(number_of_rows):
        x.append([])
        x[row_num].append(df.loc[row_num]['sepal_length'])
        x[row_num].append(df.loc[row_num]['sepal_width'])
        x[row_num].append(df.loc[row_num]['petal_length'])
        x[row_num].append(df.loc[row_num]['petal_width'])
        x[row_num].append(df.loc[row_num]['species'])
        
z=calc_z(x,w1,w2,w3,b1,b2,b3)        
p=probability_datensatz(z)
print(p)
lce=LCE(p)        
print(lce)
