#!/usr/bin/env python
# coding: utf-8

# In[28]:


import pandas as pd
data=pd.read_csv('/Users/shind/Downloads/u.user.txt',sep= "|",index_col='user_id' )
data


# In[29]:


#See the first 10 
data.head(10)


# In[30]:


#See the last 10 entries
data.tail(10)


# In[31]:


# What is the number of observations in the dataset?
data.shape
print("number of obesrvations in the dataset is:",data.shape[0])


# In[32]:


#What is the number of columns in the dataset?
print("number of columns in the dataset :",data.shape[1])


# In[37]:


#Print the name of all the columns.
print(data.columns)


# In[38]:


#What is the data type of each column?
print(data.dtypes)


# In[40]:


# Print only the occupation column
print(data['occupation'])


# In[46]:


#How many different occupations are in this dataset?
num_unique_rows = data['occupation'].nunique()
print("The different rows in the 'occupation' column are",num_unique_rows)


# In[51]:


#What is the most frequent occupation?
most_frequent_value = data['occupation'].value_counts().index[0]
print("The most frequent value in 'column_name' is:", most_frequent_value)


# In[52]:


#Describe all the columns
print(data.describe)


# In[53]:


#Summarize only the occupation column
 
occupation_summary = data['occupation'].describe()


print(occupation_summary)


# In[54]:


#What is the mean age of users?
mean_age = data['age'].mean()
print("The mean age of users is:", mean_age)


# In[59]:


# Find the value with the least occurrence
value_counts = data['age'].value_counts()
least_occurrence_value = value_counts[value_counts == value_counts.min()].index[0]
least_occurrence_value


# In[ ]:




