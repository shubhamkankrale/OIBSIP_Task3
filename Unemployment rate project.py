#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# In[4]:


df=pd.read_csv('Unemployment in india.csv')
df=pd.read_csv("Unemployment_Rate_upto_11_2020.csv")
df


# In[5]:


df.head()


# In[6]:


df.shape


# In[7]:


df.info()


# In[8]:


df.columns


# In[9]:


df.describe()


# In[10]:


df['Region'].unique()


# In[11]:


df['Region'].value_counts()


# In[12]:


print(df.isnull().sum())


# In[13]:


df.columns= ["States","Date","Frequency",
               "Estimated Unemployment Rate",
               "Estimated Employed",
               "Estimated Labour Participation Rate",
               "Region","longitude","latitude"]


# In[14]:


plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(12, 10))
sns.heatmap(df.corr())
plt.show()


# In[15]:


df.columns= ["Region","Date","Frequency",
               "Estimated Unemployment Rate","Estimated Employed",
               "Estimated Labour Participation Rate","Area",
               "longitude","latitude"]
plt.title("Indian Unemployment")
sns.histplot(x="Estimated Employed", hue="Region", data=df)
plt.show()


# In[16]:


plt.figure(figsize=(12, 10))
plt.title("Indian Unemployment")
sns.histplot(x="Estimated Unemployment Rate", hue="Region", data=df)
plt.show()


# In[17]:


unemploment = df[["Area", "Region", "Estimated Unemployment Rate"]]
figure = px.sunburst(unemploment, path=["Region", "Area"], 
                     values="Estimated Unemployment Rate", 
                     width=700, height=700, color_continuous_scale="RdY1Gn", 
                     title="Unemployment Rate in India")


# In[18]:


figure.show()


# In[ ]:





# In[ ]:




