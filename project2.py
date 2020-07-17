#!/usr/bin/env python
# coding: utf-8

# In[2]:


import json


# In[3]:


data = json.load(open("076 data.json"))
data


# In[4]:


from difflib import get_close_matches


# In[12]:


def retrive_defination(word) :
    word= word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys()))>0:
        yn = input("did you mean %s instead ? enter y for yes,or n for no " %get_close_matches(word,data.keys())[0])
        if yn == "y":
            print(data[get_close_matches(word,data.keys())[0]])
        elif yn =="n" :
            print ("the word does not exist")
        else:
            print("we didn't understand you")
    else :
        return "word not found !,please try again!!!"
word_user= input("enter your word :-->  ")
output=retrive_defination(word_user)
if type(output)==list:
    for i in output:
        print(i)
else:
    print(output)


# In[ ]:




