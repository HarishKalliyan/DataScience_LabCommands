#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np


# In[2]:


d=pd.DataFrame(np.random.rand(10,4),index=pd.date_range('1/1/2000',periods=10),columns=list('ABCD'))


# In[3]:


d.plot()


# In[4]:


sns.barplot(data=d)


# In[5]:


d.plot.bar()


# In[6]:


a=pd.DataFrame(np.random.rand(10,4),columns=['A','B','C','D'])
a.plot.bar()


# In[7]:


a=pd.DataFrame(np.random.rand(10,4),columns=['A','B','C','D'])
a.plot.bar(stacked=True)


# In[8]:


a=pd.DataFrame(np.random.rand(10,4),columns=['A','B','C','D'])
a.plot.barh(stacked=True)


# In[9]:


a=pd.DataFrame(np.random.rand(10,4),columns=['A','B','C','D'])
a.plot.box()


# In[10]:


a.plot.area()


# In[11]:


b=pd.DataFrame(np.random.rand(10,4),columns=['A','B','C','D'])
b.plot.scatter(x='A',y='B')


# In[12]:


data=[1,2,3,4,5]
data


# In[13]:


df=pd.DataFrame(data)
df


# In[14]:


df[0]


# In[15]:


df[0][3]


# In[16]:


x=['Arun',94],['Neelu',80],['Ryan',96],['Chris',77]
y=pd.DataFrame(x)


# In[17]:


y


# In[18]:


y.iloc[2]


# In[19]:


y[0:][2:3]


# In[20]:


c=pd.DataFrame(x,columns=['Name','Age'])
c


# In[21]:


c.plot.bar()


# In[22]:


c.plot.barh()


# In[23]:


c.plot.scatter(x='Name',y='Age')


# In[24]:


ds=['Arun',94,'CSE'],['Neelu',80,'IT'],['Ryan',96,'IT'],['Chris',77,'CSE']


# In[25]:


dw=pd.DataFrame(ds)
dw


# In[26]:


dw=pd.DataFrame(ds,columns=['Name','Age','Department'])
dw


# In[27]:


st={'Name':['Andrew','Bishop','Charles','Dickens','Enzo'],'Age':[21,23,22,25,24],'Department':['CSE','IT','CSD','CSBS','ADS']}
st


# In[28]:


se=pd.DataFrame(st)
se


# In[29]:


op=pd.DataFrame(st,columns=[],index=['First','Second','Third','Fourth','Fifth'])


# In[30]:


op


# In[31]:


p=pd.DataFrame(st,columns=['Name','Age','Department'],index=['First','Second','Third','Fourth','Fifth'])
p


# In[32]:


p.plot()


# In[ ]:




