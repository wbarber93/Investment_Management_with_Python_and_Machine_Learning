#!/usr/bin/env python
# coding: utf-8

# In[39]:


prices_a = [8.70, 8.91, 8.71]


# In[40]:


8.91/8.70 - 1


# In[41]:


8.71/8.91 - 1


# In[42]:


prices_a[1:]


# In[43]:


prices_a[:-1]


# In[44]:


#prices_a[1:]/prices_a[:-1] - 1 doesn't work as Python doesn't treat lists as vectors. Have to use Numpy/Pandas


# In[45]:


import numpy as np


# In[46]:


prices_a = np.array([8.70, 8.91, 8.71])
prices_a


# In[47]:


prices_a[1:]/prices_a[:-1] - 1


# In[50]:


import pandas as pd
prices = pd.DataFrame({"BLUE":[8.70, 8.91, 8.71, 8.43, 8.73], 
                       "ORANGE":[10.66, 11.08, 10.71, 11.59, 12.11]})


# In[52]:


prices


# In[53]:


prices.iloc[1:]


# In[54]:


prices.iloc[:-1]


# In[56]:


prices.iloc[1:]/prices.iloc[:-1]


# In[60]:


prices.iloc[1:].values/prices.iloc[:-1] - 1


# In[62]:


prices.iloc[1:]/prices.iloc[:-1].values - 1


# In[65]:


prices


# In[68]:


prices/prices.shift(1) -1


# In[70]:


prices


# In[71]:


prices.pct_change()


# In[72]:


prices = pd.read_csv('sample_prices.csv')
prices


# In[76]:


returns = prices.pct_change()
returns


# In[77]:


prices.plot()


# In[78]:


returns.plot.bar()


# In[79]:


returns.std()


# In[80]:


returns.mean()


# In[81]:


returns


# In[82]:


returns+1


# In[86]:


np.prod(returns+1)-1


# In[87]:


(returns+1).prod()-1


# In[88]:


(((returns+1).prod()-1)*100).round(2)


# In[91]:


## Annualization

rm = 0.01
(1+rm)**12-1


# In[92]:


rq = 0.04
(1+rq)**4 - 1


# In[93]:


rd = 0.0001
(1+rd)**252-1


# In[ ]:




