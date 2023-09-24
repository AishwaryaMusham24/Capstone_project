#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


import matplotlib.pyplot as plt


# In[19]:


x = pd.read_csv("C:/Capstone_Project/Adidas_US_Sales_Dataset.csv")
x


# In[20]:


#To find the first five rows in a dataset
x.head()


# In[21]:


x.info()


# In[22]:


#To find the statistical values of the data
x.describe()


# In[23]:


df = pd.DataFrame(x)
df


# In[24]:


#To find the average of unit products sold by product
df = pd.DataFrame(x)
Average_data = df.groupby('Product')['Units Sold']
print("Average of the units sold:", Average_data)
Max_of_data = Average_data.max()
print("Maximum of average product", Max_of_data)


# In[26]:


#Total number of sales by sales method
df = pd.DataFrame(x)
count_data = df.groupby(['Sales Method']).count()
count_data


# In[27]:


#Finding the average of operating margin by sales method
df = pd.DataFrame(x)
Profit = df.groupby('Sales Method')['Operating Margin']
print("Average of the Operating Margin:", Profit)
Max_of_data = Profit.max()
print("Maximum of average Operating Margin", Max_of_data)


# In[28]:


#The average units sold of sales method by region
df = pd.DataFrame(x)
sales_data = df.groupby(['Region','Sales Method'])['Operating Margin']
print("Avearge of the units sold:", sales_data)
Max_of_data = sales_data.max()
print("Maximum of ", Max_of_data)


# In[29]:


#To find the minimum units sold in region by sales method
df = pd.DataFrame(x)
less_sales = df.groupby('Region')['Sales Method']
print("Average of the Operating Margin:", less_sales)
Min_of_data = less_sales.min()
print("Less number of sales", Min_of_data)


# In[30]:


#To find the average of operating margin by product
df = pd.DataFrame(x)
Average_data = df.groupby(['Product'])['Operating Margin']
print("Avearge of the units sold:", Average_data)
Max_of_data = Average_data.max()
print("Maximum of average product", Max_of_data)

