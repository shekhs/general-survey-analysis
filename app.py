#!/usr/bin/env python
# coding: utf-8

# In[110]:


import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import plotly.graph_objects as go


# In[22]:


df = pd.read_csv("dataset.csv")


# In[23]:


df.head()


# In[24]:


df.shape


# In[26]:


#df = df[["sex","race","age","degree","wrkstat","income","happy"]]


# In[27]:


#sns.pairplot(df,x_vars=["sex","race","age","degree","wrkstat"],y_vars="income")


# In[28]:


st.dataframe(df)


# In[30]:


cols = df.columns


# In[34]:


pick_cols = st.selectbox("Count by column: ",cols)


# In[78]:


df["number"] = 0
df_count = df.groupby(pick_cols).count()
df_count = pd.DataFrame(df_count["number"])
df_count["percent"] = (df_count.number/df_count.number.sum())*100


# In[79]:


df_count.head()


# In[80]:


st.dataframe(df_count)


# In[103]:


multi_cols  = st.multiselect("Multiple columns ofr correlation",cols,default=["sex"])
multi_sel_col_df = df[multi_cols]


# In[104]:


st.dataframe(multi_sel_col_df)


# In[105]:


multi_cols2 = st.multiselect("multi select grouped by:",cols,default=["sex"])
multi_group=df[multi_cols2].groupby(multi_cols2).size().reset_index(name="number")
multi_group["Pc"] = (multi_group.number/multi_group.number.sum())*100


# In[106]:


st.dataframe(multi_group)


# #### Visualisation

# In[125]:


viz = st.selectbox("Viz by column",cols)

df_viz = df.groupby(viz).count()


# In[128]:


df_viz = pd.DataFrame(df_viz["number"])
df_viz["percent"] = (df_viz.number/df_viz.number.sum())*100


# In[129]:


df_viz.head()


# In[131]:


df_viz["X-axis"] = df_viz.index


# In[132]:


fig = go.Figure(data=[go.Pie(labels=df_viz["X-axis"],values=df_viz["number"])])


# In[133]:


st.plotly_chart(fig)


# In[ ]:




