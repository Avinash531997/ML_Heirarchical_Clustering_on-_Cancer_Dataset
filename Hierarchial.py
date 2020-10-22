#!/usr/bin/env python
# coding: utf-8

# In[13]:


import numpy as np                                  
import pandas as pd
import numpy.matlib
import matplotlib.pyplot as plt



#Compute the Distance
def EuclidianDist(a,b):                                                       
    return np.sqrt(np.sum((a-b)**2))

class hacAVG:
    #class hacAVG Created
    def __init__(self):                                                
        pass
    
    def CLUSTERING(self , x):
        self.x = x
        self.no_tup,self.no_features= x.shape                          
        self.distance=[]
      
        self.distance= np.zeros([self.no_tup, self.no_tup])
        b=[]
        #Creating SIMILARITY MATRIX
        for i in range(self.no_tup):                                   
            t=[]
            for j in range (self.no_tup):
                a= EuclidianDist(self.x[i],self.x[j])
                t.append(a)
            b.append(t)
        for i in range(self.no_tup):
            for j in range (self.no_tup):
                if i!=j:
                    self.distance[i][j]=b[i][j]
                else:
                    self.distance[i][j]=9999999
        clust=[]
        for iter in range(self.no_tup-1):               
            t=np.argmin(self.distance)
            row_no=t//self.no_tup
            col_no=t%self.no_tup
            b=[row_no,col_no]
            clust.append(b)
            self.UPDATE_MATRIX(self.distance,row_no,col_no)
        fin=self.CLUSTER_CREATE(clust)
        return self.CLUSTER_NO(fin)
    
    #SIMILARITY MATRIX UPDATED    
    def UPDATE_MATRIX(self, m, r, c):                                  
        for j in range (self.no_tup):
            if j!=r:
                m[j][r]=m[r][j]=(m[c][j]+m[r][j])/2
        for j in range (self.no_tup):
            m[j][c]=m[c][j]=9999999
       
    #CREATE CLUSTER
    def CLUSTER_CREATE(self, c):                                       
        a=[[] for q in range(2)]
        for r in reversed(range(len(c))):
            if a[0]==[] and a[1]==[]:
                a[0].append(c[r][0])
                a[1].append(c[r][1])
            else:
                if c[r][0] in a[0]:
                    a[0].append(c[r][1])
                if c[r][0] in a[1]:
                    a[1].append(c[r][1])
        return a
    #ASSIGN CLUSTER NUMBER to CLUSTERS
    def CLUSTER_NO(self, clusters):                                      
        n= np.empty(self.no_tup)
        for i,j in enumerate(clusters):
            for l in j:
                n[l]=i
        return n
class hacMIN:
     #Class hacMIN Created 
    def __init__(self):                                                   
        pass
    
    def CLUSTERING(self , x):
        self.x = x
        self.no_tup,self.no_features= x.shape                              
        self.distance=[]
      
        self.distance= np.zeros([self.no_tup, self.no_tup])
        b=[]
        #SIMILARITY MATRIX FORMED
        for i in range(self.no_tup):                                        
            t=[]
            for j in range (self.no_tup):
                a= EuclidianDist(self.x[i],self.x[j])
                t.append(a)
            b.append(t)
        for i in range(self.no_tup):
            for j in range (self.no_tup):
                if i!=j:
                    self.distance[i][j]=b[i][j]
                else:
                    self.distance[i][j]=9999999
        clust=[]
        for iter in range(self.no_tup-1):                                 
            t=np.argmin(self.distance)
            row_no=t//self.no_tup
            col_no=t%self.no_tup
            b=[row_no,col_no]
            clust.append(b)
            self.UPDATE_MATRIX(self.distance,row_no,col_no)
        fin=self.CLUSTER_CREATE(clust)
        return self.CLUSTER_NO(fin)
    
    #SIMILARITY MATRIX UPDATED    
    def UPDATE_MATRIX(self, m, r, c):                                    
        for j in range (self.no_tup):
            if j!=r:
                m[j][r]=m[r][j]=min(m[c][j],m[r][j])
        for j in range (self.no_tup):
            m[j][c]=m[c][j]=9999999
     
   #CREATING CLUSTERS 
    def CLUSTER_CREATE(self, c):                                         
        a=[[] for q in range(2)]
        for r in reversed(range(len(c))):
            if a[0]==[] and a[1]==[]:
                a[0].append(c[r][0])
                a[1].append(c[r][1])
            else:
                if c[r][0] in a[0]:
                    a[0].append(c[r][1])
                if c[r][0] in a[1]:
                    a[1].append(c[r][1])
        return a
    
    #ASSIGNING CLUSTER NUMBER TO CLUSTERS
    def CLUSTER_NO(self, clusters):                                     
        n= np.empty(self.no_tup)
        for i,j in enumerate(clusters):
            for l in j:
                n[l]=i
        return n

    
class hacCOMPLETE:
    #CLASS hacCOMPLETE CREATED
    def __init__(self):                                                
        pass
    
    def CLUSTERING(self , x):
        self.x = x
        self.no_tup,self.no_features= x.shape                          
        self.distance=[]
      
        self.distance= np.zeros([self.no_tup, self.no_tup])
        b=[]
        #SIMILARITY MATRIX CREATED
        for i in range(self.no_tup):                                    
            t=[]
            for j in range (self.no_tup):
                a= EuclidianDist(self.x[i],self.x[j])
                t.append(a)
            b.append(t)
        for i in range(self.no_tup):
            for j in range (self.no_tup):
                if i!=j:
                    self.distance[i][j]=b[i][j]
                else:
                    self.distance[i][j]=9999999
        clust=[]
        for iter in range(self.no_tup-1):                                  
            t=np.argmin(self.distance)
            row_no=t//self.no_tup
            col_no=t%self.no_tup
            b=[row_no,col_no]
            clust.append(b)
            self.UPDATE_MATRIX(self.distance,row_no,col_no)
        fin=self.CLUSTER_CREATE(clust)
        return self.CLUSTER_NO(fin)
    
     #SIMILARITY MATRIX UPDATED   
    def UPDATE_MATRIX(self, m, r, c):                                       
        for j in range (self.no_tup):
            if j!=r:
                m[j][r]=m[r][j]=max(m[c][j],m[r][j])
        for j in range (self.no_tup):
            m[j][c]=m[c][j]=9999999
    
    #CREATING CLUSTERS
    def CLUSTER_CREATE(self, c):                                            
        a=[[] for q in range(2)]
        for r in reversed(range(len(c))):
            if a[0]==[] and a[1]==[]:
                a[0].append(c[r][0])
                a[1].append(c[r][1])
            else:
                if c[r][0] in a[0]:
                    a[0].append(c[r][1])
                if c[r][0] in a[1]:
                    a[1].append(c[r][1])
        return a
    
    #ASSIGNING CLUSTER NUMBER TO CLUSTERS
    def CLUSTER_NO(self, clusters):                                       
        n= np.empty(self.no_tup)
        for i,j in enumerate(clusters):
            for l in j:
                n[l]=i
        return n

#READING THE INPUT DATA SET
data = pd.read_csv('cancer.csv', delimiter=',')                           
data= data.to_numpy()
data= np.delete(data,[0,1,32],axis=1)
k= hacAVG()
pri=k.CLUSTERING(data)
q= HACmin()
qri=q.CLUSTERING(data)
z= hacCOMPLETE()
pri3=z.CLUSTERING(data)

print("CASE 1: SINGLE_LINKAGE ")
for i in range(len(set(qri))):
    print("Number of Data Points in CLUSTER", i," is ", list(qri).count(i))


clr = ['red', 'green', 'blue','cyan','magenta', 'orange', 'brown', 'purple','olive','lime','black','aqua','teal','silver','peru']
X=data
Y_Val=qri
plt.xlabel('RADIUS_MEAN')
plt.ylabel('TEXTURE_MEAN')
for i in range(len(set(Y_Val))):
    plt.scatter(
        X[Y_Val == i, 0], X[Y_Val == i, 1],
        s=50, c=clr[i%len(clr)],
        marker='+',label=i
    )


plt.legend(scatterpoints=1)
plt.grid()
plt.show()

print("CASE 2: COMPLETE_LINKAGE")
for i in range(len(set(pri3))):
    print("Number of Data Points in CLUSTER", i," is ", list(pri3).count(i))

clr = ['red', 'green', 'blue','cyan','magenta', 'orange', 'brown', 'purple','olive','lime','black','aqua','teal','silver','peru']
X=data
Y_Val=pri3
plt.xlabel('RADIUS_MEAN')
plt.ylabel('TEXTURE_MEAN')
for i in range(len(set(Y_Val))):
    plt.scatter(
        X[Y_Val == i, 0], X[Y_Val == i, 1],
        s=50, c=clr[i%len(clr)],
        marker='+',label=i
    )


plt.legend(scatterpoints=1)
plt.grid()
plt.show()

print("CASE 3 : AVERAGE __ LINKAGE")
for i in range(len(set(pri))):
    print("Number of Data Points in CLUSTER ", i," is ", list(pri).count(i))


clr = ['red', 'green', 'blue','cyan','magenta', 'orange', 'brown', 'purple','olive','lime','black','aqua','teal','silver','peru']
X=data
Y_Val=pri
plt.xlabel('RADIUS_MEAN')
plt.ylabel('TEXTURE_MEAN')
for i in range(len(set(Y_Val))):
    plt.scatter(
        X[Y_Val == i, 0], X[Y_Val == i, 1],
        s=50, c=clr[i%len(clr)],
        marker='+',label=i
    )


plt.legend(scatterpoints=1)
plt.grid()
plt.show()


# In[ ]:




