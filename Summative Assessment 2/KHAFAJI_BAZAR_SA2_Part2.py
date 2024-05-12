#!/usr/bin/env python
# coding: utf-8

# In[16]:


get_ipython().system('pip install scipy')
get_ipython().system('pip install polars')


# In[85]:


import pandas as pd
import numpy as np
import polars as pl
from scipy.stats import shapiro


# In[40]:


eth1 = pl.read_csv("BAZAR_KHAFAJI_ETHSD_AUG2017_APR2024.csv", infer_schema_length=2000)    .select(pl.col("timestamp"), pl.col("open"), pl.col("high"), pl.col("low"), pl.col("close"), pl.col("volume"), pl.col("return"))    .fill_nan(None)    .drop_nulls()
print(eth1)


# In[38]:


mintime = eth1.select(pl.min("timestamp"))

print(mintime)


# In[77]:


eth2 = pl.read_csv("ETH_1min.csv", infer_schema_length=2000)    .select(pl.col("Unix Timestamp"), pl.col("Open"), pl.col("High"), pl.col("Low"), pl.col("Close"), pl.col("Volume"))    .fill_nan(None)    .drop_nulls()    .with_columns(Return = pl.col("Close")-pl.col("Open"))

print(eth2)


# In[78]:


mintime2 = eth2.select(pl.min("Unix Timestamp"))

print(mintime2)


# In[79]:


filter = eth2.filter(pl.col("Unix Timestamp") < mintime)

print(filter)


# In[71]:


neweth = eth2.filter(pl.col("Unix Timestamp") < mintime).select(
    pl.col("Unix Timestamp").alias("timestamp"),
    pl.col("Open").cast(pl.Float64).alias("open"),
    pl.col("High").cast(pl.Float64).alias("high"),
    pl.col("Low").cast(pl.Float64).alias("low"),
    pl.col("Close").cast(pl.Float64).alias("close"),
    pl.col("Volume").cast(pl.Float64).alias("volume"),
    pl.col("Return").cast(pl.Float64).alias("return")
    )

print(neweth)


# In[80]:


ethcombined = pl.concat([eth1, neweth])

print(ethcombined)


# In[114]:


ethreturns = ethcombined.select("return")

print("Shapiro-Wilk Test:", statistic)
print("P-value:", p_value)

statistic, p_value = shapiro(np.squeeze(ethreturns.to_numpy() ) )

alpha = 0.05
if p_value < alpha:
    print("Reject null hypothesis: Data is not normally distributed")
else:
    print("Fail to reject null hypothesis: Data may be normally distributed")

