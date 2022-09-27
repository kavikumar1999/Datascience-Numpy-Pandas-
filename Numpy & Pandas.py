#!/usr/bin/env python
# coding: utf-8

# In[91]:


import numpy as np
import pandas as pd


# In[92]:


book_data = pd.read_csv("C://Training//book.csv")
print(book_data)


# In[93]:


Avg_book_data = book_data.max()
print(Avg_book_data)


# In[94]:


Avg_book_data = book_data.min()
print(Avg_book_data)


# In[95]:



Avg_book_data_mean = np.mean(book_data)
print(Avg_book_data_mean)


# In[96]:


book_data.head(5)


# In[97]:


book_data.tail(4)


# In[98]:


book_data.dropna(axis=0,inplace=True)
print(book_data)


# In[99]:


book_data.info()


# In[100]:


print(book_data.describe())


# # Numpy
# 

# In[101]:



#The function returns evenly spaced numbers over a specified interval defined by the first two arguments
#numpy.linspace(start,stop,num=11,endpoint=True)

np.linspace(0,10,11)


# In[102]:


np.linspace(0,10,11,endpoint=False)


# In[103]:


#repeat
#numpy.repeat(a, repeat, axis=None)
#np.repeat(3,5)
np.repeat('2022',5)


# In[104]:


sales_2022 = pd.DataFrame([['chair',20],['sofa',24],['table',15]], columns=['product', 'sales_units'])
sales_2021 = pd.DataFrame([['chair',25],['sofa',10],['shelf',10]], columns=['product', 'sales_units'])


# In[105]:


sales_2022['year']=np.repeat(2022,sales_2022.shape[0])
sales_2021['year']=np.repeat(2021,sales_2021.shape[0])


# In[106]:


sales = pd.concat([sales_2022,sales_2021], ignore_index=True)
sales


# # RANDOM
# 

# In[107]:


#numpy.random.randint(low,high=none,size=none)
#toss a coin 5 times
np.random.randint(2,size=5)


# In[108]:


#Dice
np.random.randint(1,7)


# In[109]:


np.random.randint(1,7,size=10)


# # HEIGHT AND WEIGHT
# 

# In[110]:


#y=a+bx -> x is independent variable, y is dependent variable, b slop, a intercept
#numpy.ployfit
df=pd.read_csv('C://Training//height_and_weight.csv')
df


# # SCATTER PLOT

# In[112]:



import matplotlib.pyplot as plt
df.plot(kind='scatter', x='Height', y='Weight', color='blue', alpha=0.3,figsize=(4,3))
#title, xlabel, ylabel
plt.title('Relationship between Height and Weight', size=24)
plt.xlabel('Height (inches)', size=18)
plt.ylabel('Weight (pounds)', size=18)

