#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd

prices = pd.read_csv('sample_prices.csv')

pct_returns = prices.pct_change()
pct_returns


# In[7]:


drop_returns = returns.dropna()
drop_returns


# In[9]:


risk = returns.std()
risk


# In[12]:


deviations = returns - returns.mean()
squared_deviations = deviations**2

variance = squared_deviations.mean()

volatility = variance**0.5
volatility


# In[15]:


number_of_obs = returns.shape[0]

variance = squared_deviations.sum()/(number_of_obs - 1)

volatility = variance**0.5
volatility


# In[16]:


returns.std()


# In[17]:


returns.std()*(12**0.5)


# In[ ]:




