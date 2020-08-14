#!/usr/bin/env python
# coding: utf-8

# In[1]:


N=int(input())
arr=[]
for i in range(N):
    num,Ox=map(str,input().split(' '))
    arr.append(Ox)
    
for i in arr:
    if i in lis:
        print(bin(int(i, 16))[2:])
    else:
        print('0'+bin(int(i, 16))[2:])


# In[ ]:




