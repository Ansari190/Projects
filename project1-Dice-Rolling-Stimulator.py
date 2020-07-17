#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math


# In[ ]:


import random 
x= random.randint(1,6)

import random


t = 'y'

#for y in range(x):
while t == 'y':
    x = random.randint(1,6)
    #x = x+i
    if x == 1:
        print(" ___________")
        print("|           |")
        print("|     o     |")
        print("|           |")
        print("|___________|")

    if x == 2:
        print(" ___________")
        print("|           |")
        print("|   o   o   |")
        print("|           |")
        print("|___________|")

    if x == 3:
        print(" ___________ ")
        print("|           |")
        print("|o    o   o |")
        print("|           |")
        print("|___________|") 

    if x == 4:
        print(" ___________ ")
        print("| O       O |")
        print("|           |")
        print("| O       O |")
        print("|___________|")

    if x == 5:
        print( "___________ ")
        print("| O        O|")
        print("|     O     |")
        print("| O        O|")
        print("|___________|")

    if x == 6:
        print(" ___________ ")
        print("|O        O |")
        print("|O        O |")
        print("|O        O |")
        print("|___________|")

    t = input("Press y to roll again : ")


# In[ ]:




