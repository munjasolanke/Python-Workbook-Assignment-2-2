#!/usr/bin/env python
# coding: utf-8

# In[4]:



#Week-7-Homework
#Assignment-2-2
import pandas as pd
from sqlalchemy import create_engine
engine = create_engine(r"sqlite:///C:\MUNJA_DATA\Courses\Data Visualization\Week-7\learn-data-analysis-w-python-master\datasets\salesdata.db")

# Getting the table names 
sql = "select name from sqlite_master"
"where type = 'table';"

sales_data_df = pd.read_sql(sql, engine)
sales_data_df


# In[5]:


# Selecting the table from the database
sql_table = "select * from scores"
score_data_df = pd.read_sql(sql_table, engine)
score_data_df.head()


# In[ ]:




