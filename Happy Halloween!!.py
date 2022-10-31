#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

## Read in Data
pumpkins = pd.read_csv("pumpkins.csv")


# In[2]:


print(pumpkins.head())


# In[3]:


print(pumpkins.info())


# In[4]:


#shape, how many values
pumpkins.shape


# In[5]:


sns.histplot(pumpkins.Low_Price)
plt.show()
plt.clf()


# In[6]:


sns.histplot(pumpkins.High_Price)
plt.show()
plt.clf()


# In[7]:


#print unique color values
print(pumpkins['Color'].unique())


# In[8]:


#print unique color values
print(pumpkins['Variety'].unique())


# In[9]:


#print unique color values
print(pumpkins['Item_Size'].unique())


# In[10]:


pumpkins2 = pumpkins[["City_Name","Low_Price","High_Price"]]


# In[11]:


#highest price pumpkins
newpump1 = pumpkins2.groupby('City_Name')['High_Price'].mean().sort_values(ascending=False)
print(newpump1)


# In[12]:


pumpkins4 = pumpkins[["Color","Low_Price","High_Price"]]


# In[13]:


pumpkins4.groupby(['Color']).mean()


# In[14]:


newpump2 = pumpkins.groupby('Origin')['Origin'].count().sort_values(ascending=False)
print(newpump2)


# In[15]:


sns.displot(pumpkins, x="Low_Price", col="Item_Size")


# In[16]:


sns.displot(pumpkins, x="Low_Price", col="Color")


# In[ ]:




