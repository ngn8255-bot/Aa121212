#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
answer=45
chance=1
while chance<=3:
    guess=int(input('input your guess: '))
    if guess>answer:
        print('it is larger')
        chance+=1
    elif guess<answer:
        print('it is so small')
        chance+=1
    else:
        print('it is right')
        sys.exit()
if chance>3:
    print('right anwser is 45')
else:
    print('you are right')
        


# In[ ]:




