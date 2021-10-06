#!/usr/bin/env python
# coding: utf-8

# In[45]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[25]:


df = pd.read_csv('D:/food_delivery_datasets.csv')


# In[32]:


df.head()


# In[40]:


#create new colomn in date-time object(DTO)
df['Order_Date_DTO'] = pd.to_datetime(df['date_time'])
df.head()


# In[41]:


#Create new column in date-time object (DTO)
df['Order_Date_DTO'] = pd.to_datetime(df['date_time'])

#Extraction the hours data
df['Hour'] = df['Order_Date_DTO'].dt.hour
df.head()


# In[42]:


result=df.groupby(["Hour"]).count()
result


# In[49]:


#Plotting
results3 = df.groupby(['Hour'])['cust_id'].count()
hours = [hour for hour, df in df.groupby('Hour')]

plt.plot(hours, results3)
plt.xticks(hours)
plt.xlabel('Hour')
plt.ylabel('Number of Orders')
plt.grid()
plt.show()


# In[ ]:




