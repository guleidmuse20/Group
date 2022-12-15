#!/usr/bin/env python
# coding: utf-8

# In[118]:


import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.model_selection import train_test_split
import numpy as nu
import random as ran


# In[121]:




summary, labels = nu.arange(0,1248), nu.arange(0,1248)

X_train, X_test, y_train, y_test = train_test_split(summary, labels, test_size=0.35)
X = datas.copy()
Y= pd.DataFrame(columns = df['weather'])
model = DecisionTreeClassifier()
model.fit(X_train.reshape(-1,1),y_train) 
p = model.predict(X_train.reshape(-1,1))
print(p)


# In[126]:



for i in p:
    num = ran.randrange(0,6)
    if i < 100:
        if num == 1:
            print("i")
        if num == 2:
            print("am")
        if num == 3:
            print("the")
        if num == 4:
            print("car")
        if num == 5:
            print("duck")
        if num == 6:
            print("in")   
    if i < 200:
        if num == 1:
            print("an")
        if num == 2:
            print("elephant")
        if num == 3:
            print("big")
        if num == 4:
            print("truck")
        if num == 5:
            print("show")
        if num == 6:
            print("at")
    if i < 300:
        if num == 1:
            print("milk")
        if num == 2:
            print("today")
        if num == 3:
            print("sleep")
        if num == 4:
            print("under")
        if num == 5:
            print("left")
        if num == 6:
            print("have")
    if i < 400:
        if num == 1:
            print("a")
        if num == 2:
            print("up")
        if num == 3:
            print("school")
        if num == 4:
            print("study")
        if num == 5:
            print("duck")
        if num == 6:
            print("be")
    if i < 500:
        if num == 1:
            print("around")
        if num == 2:
            print("through")
        if num == 3:
            print("small")
        if num == 4:
            print("back")
        if num == 5:
            print("He")
        if num == 6:
            print("giraffe")
    if i < 600:
        if num == 1:
            print("name")
        if num == 2:
            print("she")
        if num == 3:
            print("very")
        if num == 4:
            print("tired")
        if num == 5:
            print("duck")
        if num == 5:
            print("lived on")
    if i < 700:
        if num == 1:
            print("went")
        if num == 2:
            print("zoo")
        if num == 3:
            print("eating")
        if num == 4:
            print("drinking")
        if num == 5:
            print("project")
        if num == 6:
            print("")
    if i < 800:
        if num == 1:
            print("pause")
        if num == 2:
            print("went")
        if num == 3:
            print("stayed")
        if num == 4:
            print("make")
        if num == 5:
            print("right")
        if num == 6:
            print("it")
   
    if i < 900:
        if num == 1:
            print("worked")
        if num == 2:
            print("at")
        if num == 3:
            print("then")
        if num == 4:
            print("after")
        if num == 5:
            print("on")
        if num == 6:
            print("the")
    if i < 1000:
        if num == 1:
            print("they")
        if num == 2:
            print("played")
        if num == 3:
            print("park")
        if num == 4:
            print("sit")
        if num == 5:
            print("open")
        if num == 6:
            print("duck")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




