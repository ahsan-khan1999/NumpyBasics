#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[7]:


data = np.random.randn(2,4)


# In[8]:


data


# In[34]:


generateArray = np.arange(10)
        

generateArray

# In[10]:


data.ndim


# In[11]:


data.shape


# In[12]:


b=np.array([[[100]]])


# In[13]:


b.ndim


# In[14]:


b.shape


# In[18]:


threeDim = np.array([[1,2,3],[1,2,3],[1,2,3]])


# In[19]:


threeDim


# In[33]:


threeDim.size


# In[25]:


threeDim.ndim


# In[28]:


checkDim = np.array([[[[[[[[1]]]]]]]])


# In[29]:


checkDim.ndim


# In[31]:


checkDim.data


# In[32]:


checkDim.size


# In[ ]:





# In[ ]:





# In[20]:


d = np.arange(30).reshape(3,5,2)


# In[21]:


d


# In[22]:


e = np.arange(30).reshape(5,3,2)
e


# In[37]:


e.sort


# In[38]:


e


# In[24]:


d.ndim


# In[48]:


m1 = np.arange(12).reshape(4,3)


# In[49]:


m2=np.array([[1,2,3],[2,3,4],[3,4,5],[4,5,6]])


# In[50]:


m1.shape = m2.shape


# In[51]:


m3 = m1 * m2


# ### 

# In[52]:


m3


# In[53]:


m1.shape


# m2.shape

# In[57]:


m4 = np.arange(12).reshape(3,4)


# 

# In[58]:


m1 * m4


# In[62]:


m1@m3 # python 3 feature


# In[63]:


np.dot(m1,m4) # 2nd way as of m1@m4


# In[64]:


m1.dot(m4)


# In[66]:


m1 + m3


# In[67]:


m1 - m3


# In[68]:


m1 / m3


# In[73]:


a =np.array([32,34,56.],dtype = "int")


# In[75]:


a.astype("float32")


# In[82]:


b = np.asarray(np.array([1,2,3]),dtype= "float32")


# In[83]:


b


# In[92]:


np.ones((0,10))


# In[89]:


np.zeros((2,10))


# In[90]:


np.empty(5) # usually returns zero and if system have garbage value it transfer it into array application  onehot encodeing


# In[93]:


np.ones((3,4)) * 5


# In[96]:


z =np.full((3,4),4)


# In[97]:


np.ones_like(z)


# In[98]:


lista = [1,2,3,5,6,7]# type of list is list type of list element is int slicing return an array of element and index returns a single element


# In[99]:


x = np.arange(36).reshape(6,6)


# In[100]:


x


# In[101]:


x[2,3]# x[2][3]


# In[104]:


x[2:6,2:4]


# In[ ]:





# In[ ]:




