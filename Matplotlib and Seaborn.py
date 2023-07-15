#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np


# In[2]:


x=np.arange(0,5,0.1)
y=np.sin(x)
z=np.cos(x)
plt.plot(x,y)
plt.plot(x,z)
plt.show()


# In[3]:


x=[1,2,3,4,5,6,7,8,9,10]
y=[23,14,19,6,7,28,32,20,9,17]
plt.plot(x,y)
plt.title("Run Rate")
plt.xlabel("Overs")
plt.ylabel("Runs Per Over")
plt.show()


# In[4]:


x=[1,2,3,4,5,6,7,8,9,10]
ind=[23,14,19,6,7,28,32,20,9,17]
pak=[19,23,32,19,30,8,17,21,24,18]
plt.plot(x,ind)
plt.plot(x,pak)
plt.title("Run Rate")
plt.xlabel("Overs")
plt.ylabel("Runs Per Over")
plt.legend(ind)
plt.show()


# In[5]:


#New Exercise


# In[6]:


import pandas as pd
d=pd.read_csv('C:/president_heights.csv')


# In[7]:


d


# In[8]:


d.plot()


# In[9]:


d.plot.bar()


# In[10]:


d.plot.bar(stacked=True)


# In[11]:


d.plot.barh()


# In[12]:


d.plot.barh(stacked=True)


# In[13]:


d.plot.box()


# In[14]:


d.plot.area()


# In[15]:


d.plot.scatter(x='order',y='height(cm)')


# In[16]:


#Seaborn Exercise


# In[17]:


import seaborn as sns


# In[18]:


sns.barplot(x='name',y='height(cm)',data=d)


# In[19]:


sns.barplot(x='name',y='height(cm)',data=d)
plt.figure(figsize=(20,10))


# In[20]:


sns.barplot(x='name',y='height(cm)',data=d)
plt.xticks(rotation=90)
plt.figure(figsize=(20,10))


# In[21]:


sns.barplot(x='name',y='height(cm)',data=d)
plt.xticks(rotation=90)
plt.ylim(100,200)
plt.figure(figsize=(20,10))


# In[22]:


sns.barplot(x='name',y='height(cm)',data=d,color="grey")
plt.xticks(rotation=90)
plt.ylim(100,200)
plt.figure(figsize=(20,10))


# In[23]:


sns.barplot(x='order',y='height(cm)',data=d,color="maroon")
plt.xticks(rotation=90)
plt.title('President Heights')
plt.ylim(100,200)
plt.figure(figsize=(20,10))


# In[24]:


sns.barplot(x='order',y='height(cm)',data=d,color="pink")
plt.xticks(rotation=90)
plt.title('President Heights')
plt.ylim(175,190)
plt.figure(figsize=(20,10))


# In[25]:


l=d[((d['height(cm)']>=170)&(d['height(cm)']<185))]


# In[26]:


l


# In[27]:


sns.barplot(x='order',y='height(cm)',data=l,color="maroon")
plt.xticks(rotation=90)
plt.title('President Heights')
plt.ylim(100,200)
plt.figure(figsize=(20,10))


# In[28]:


a=pd.Series([1.0,1.5,1.75,2.0],index=['a','b','c','d'])


# In[29]:


a


# In[30]:


a['c']


# In[31]:


'a' in a


# In[32]:


'g' in a


# In[33]:


a.keys


# In[34]:


a.keys()


# In[35]:


list(a.items())


# In[36]:


a['e']=2.5


# In[37]:


a


# In[38]:


a["b":"d"]


# In[39]:


a[2:4]


# In[40]:


a[((a>1.5)&(a<2.5))]


# In[41]:


area=({'Chennai':81,"Bangalore":82,'Kerala':83,'Mumbai':94,'Delhi':96})
area


# In[42]:


area.keys()


# In[43]:


pop=area=pd.Series({'Chennai':81,"Bangalore":82,'Kerala':83,'Mumbai':94,'Delhi':96})


# In[44]:


area


# In[45]:


data=pd.DataFrame({'area':area,'pop':pop})


# In[46]:


data


# In[47]:


data['density']=data['pop']+data['area']


# In[48]:


data


# In[49]:


data.values


# In[50]:


data.values[2]


# In[51]:


data.values[:,1]


# In[52]:


data.iloc[0]


# In[53]:


data.iloc[0,2]


# In[54]:


data.iloc[0,2]=90


# In[55]:


data


# In[56]:


data[data.density>180]


# In[57]:


data.iloc[3,0]=95


# In[58]:


data


# In[59]:


data.isnull()


# In[60]:


s=pd.Series([1,np.nan,2,None,3],index=['a','b','c','d','e'])


# In[61]:


s


# In[62]:


s.fillna(0)


# In[63]:


#Forword filling
s.fillna(method='ffill')


# In[64]:


#Backward filling
s.fillna(method='bfill')


# In[ ]:




