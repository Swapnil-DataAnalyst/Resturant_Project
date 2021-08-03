#!/usr/bin/env python
# coding: utf-8

# In[4]:


# importing required libraries
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd


# In[3]:


#reading the dataset
total_dish = pd.read_csv('C:/Users/SONY/Desktop/DataSet1/dish.csv')


# In[5]:


total_dish.head()


# In[15]:


# bar plot of top 10 resturant serving max dishes
plt.figure(figsize=(10,5))
sns.set_context("paper", font_scale = 2, rc = {"font.size": 20,"axes.titlesize": 25,"axes.labelsize": 0})   
sns.barplot(data = total_dish, x = df['Resturant'][0:10], y =df['Count of Dish_name'][0:10])
plt.title('Number of restaurants serving maximum food (TOP 10)')
plt.xticks(rotation=90)
plt.show()


# In[33]:


#reading the dataset
type_dish = pd.read_csv('C:/Users/SONY/Desktop/DataSet1/count_dish.csv')


# In[34]:


type_dish.head()


# In[35]:


# bar plot of top 10 dishes liked by people
plt.figure(figsize=(10,5))
sns.set_context("paper", font_scale = 2, rc = {"font.size": 20,"axes.titlesize": 25,"axes.labelsize": 0})   
sns.barplot(data = type_dish, x = type_dish['Dish_Name'][0:10], y =type_dish['Count of Dish_name'][0:10])
plt.title('TOP 10 Dishes liked by People of New-York')
plt.xticks(rotation=90)
plt.show()


# In[37]:


# bar plot of least 10 dishes liked by people
plt.figure(figsize=(10,5))

sns.barplot(data = type_dish, x = type_dish['Dish_Name'].tail(10), y =type_dish['Count of Dish_name'].tail(10))
plt.xticks(rotation=90)
plt.title('Least 10 Dishes liked by People of New-York')
plt.show()


# In[42]:


#reading the dataset
avg_price = pd.read_csv('C:/Users/SONY/Desktop/DataSet1/avg_price.csv')


# In[43]:


avg_price.head()


# In[44]:


# bar plot of top 10 highest paid resturant 
plt.figure(figsize=(10,5))
sns.set_context("paper", font_scale = 2, rc = {"font.size": 20,"axes.titlesize": 25,"axes.labelsize": 0})   
sns.barplot(data = avg_price, x = avg_price['Restaurant'][0:10], y =avg_price['Avg_Price'][0:10])
plt.title('TOP 10 Resturants order by Average Price')
plt.xticks(rotation=90)
plt.show()


# In[61]:


#reading the dataset
cuisine = pd.read_csv('C:/Users/SONY/Desktop/DataSet1/cuisine.csv')


# In[62]:


cuisine.head()


# In[63]:


# bar plot of top 10 cuisine 
plt.figure(figsize=(10,5))
sns.set_context("paper", font_scale = 2, rc = {"font.size": 20,"axes.titlesize": 25,"axes.labelsize": 0})   
sns.barplot(data = cuisine, x = cuisine['Cuisine'][0:10], y =cuisine['Count of Cuisine'][0:10])
plt.title('TOP 10 Cuisines with maximum number of Resturant')
plt.xticks(rotation=90)
plt.show()


# In[64]:


# bar plot of least 10 cuisine
plt.figure(figsize=(10,5))

sns.barplot(data = cuisine, x = cuisine['Cuisine'].tail(10), y =cuisine['Count of Cuisine'].tail(10))
plt.xticks(rotation=90)
plt.title('Least 10 liked Cuisines')
plt.show()


# In[5]:


#reading the dataset
dish_type = pd.read_csv('C:/Users/SONY/Desktop/DataSet1/dish_type.csv')


# In[6]:


dish_type.head()


# In[7]:


# bar plot of top 10 dish types by resturant 
plt.figure(figsize=(10,5))
sns.set_context("paper", font_scale = 2, rc = {"font.size": 20,"axes.titlesize": 25,"axes.labelsize": 0})   
sns.barplot(data = dish_type, x = dish_type['Types of Dish'][0:10], y =dish_type['Count of Dish_Type'][0:10])
plt.title('TOP 10 Dishe-Types offered by maximum number of Resturant')
plt.xticks(rotation=90)
plt.show()


# In[70]:


#reading the dataset
ing = pd.read_csv('C:/Users/SONY/Desktop/DataSet1/ing.csv')


# In[71]:


ing.head()


# In[72]:


# bar plot of top 10 ingredients used in dishes 
plt.figure(figsize=(10,5))
sns.set_context("paper", font_scale = 2, rc = {"font.size": 20,"axes.titlesize": 25,"axes.labelsize": 0})   
sns.barplot(data = ing, x = ing['Ingredients'][0:10], y =ing['Used in total no.of dishes'][0:10])
plt.title('TOP 10 Ingredients used in Dishes')
plt.xticks(rotation=90)
plt.show()


# In[ ]:




