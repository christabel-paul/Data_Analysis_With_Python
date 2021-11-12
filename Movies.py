#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import seaborn as sns

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib


# In[4]:


plt.style.use('ggplot')
from matplotlib.pyplot import figure

get_ipython().run_line_magic('matplotlib', 'inline')
matplotlib.rcParams['figure.figsize'] = (12,8)

pd.options.mode.chained_assignment = None


# In[5]:


#read in data
df = pd.read_csv(r'C:\Users\chris\Documents\sql portfolio projects\4-movies\movies.csv')


# In[6]:


df.head()


# In[7]:


df.dtypes


# In[8]:


#fill in null values and change data types
df = df.fillna(0)
df['budget'].astype('int64')
df['gross'].astype('int64')
df['released'].astype(str)


# In[9]:


# create a column for release country and corrected year
df['country'] = ""
df['correctedYear'] = ""


# In[10]:


try:
    for item in df.index:       
        countryWordIndex = df['released'][item].index('(') + 1
        df['country'][item]= df['released'][item][countryWordIndex:df['released'][item].index(')')]
        yearIndex = df['released'][item].index('(') - 5  
        df['correctedYear'][item] = df['released'][item][yearIndex:(yearIndex+4)]   
except AttributeError:
    pass


# In[11]:


#drop old year released column
df.drop('year', axis=1, inplace=True)


# In[12]:


df.sort_values(by=['gross'], inplace = False,ascending = False)


# In[13]:


#drop duplicates
df.drop_duplicates()


# In[14]:


#check for outliers
df.boxplot(column = ['gross'])


# In[15]:


#scatter plot with budget vs gross revenue
plt.scatter(x=df['budget'], y=df['gross'])
plt.title('Budget vs Gross Earnings')
plt.xlabel('Budget (M)')
plt.ylabel('Gross Earnings (M)')
plt.show


# In[16]:


sns.regplot(x='budget', y='gross', data=df, scatter_kws = {"color": "black"}, line_kws = {"color": "blue"})


# In[17]:


df.corr()


# In[18]:


correlation_matrix = df.corr(method = 'pearson')
sns.heatmap(correlation_matrix, annot=True)
plt.title('Correlation Matrix for Movie Features (numeric only)')
plt.xlabel('Movie Feature')
plt.ylabel('Movie Feature')
plt.show


# In[19]:


#create a new frame with numerical values assigned to column values
df_numeric = df
for col_name in df_numeric:
    if(df_numeric[col_name].dtype == 'object'):
        df_numeric[col_name] = df_numeric[col_name].astype('category')
        df_numeric[col_name] = df_numeric[col_name].cat.codes


# In[20]:


df_numeric.head()


# In[21]:


correlation_matrix = df_numeric.corr(method = 'pearson')
sns.heatmap(correlation_matrix, annot=True)
plt.title('Correlation Matrix for Movie Features (numeric only)')
plt.xlabel('Movie Feature')
plt.ylabel('Movie Feature')
plt.show


# In[22]:


df_numeric.corr()


# In[26]:


#list all the features and there corresponding correlations
correlation_matrix = df_numeric.corr()
corr_pairs = correlation_matrix.unstack()
corr_pairs


# In[28]:


#sort the correlation pairs in order of correlation value
pd.set_option('display.max_rows', None)
sorted_pairs = corr_pairs.sort_values()
sorted_pairs


# In[ ]:


#budget and user votes had the highest correlation to gross revenue

