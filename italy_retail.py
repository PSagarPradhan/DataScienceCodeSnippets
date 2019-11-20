#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import os


# In[13]:


from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules


# In[3]:


df = pd.read_csv('italy_retail.csv')


# In[32]:


basket = (df.groupby(['InvoiceNo', 'Description'])['Quantity']
          .sum().unstack().reset_index().fillna(0)
          .set_index('InvoiceNo'))


# In[33]:


def encode_units(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1

basket_sets = basket.applymap(encode_units)


# In[35]:


frequent_itemsets = apriori(basket_sets, min_support=0.1, use_colnames=True)


# In[38]:


rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=1)
rules.head()

