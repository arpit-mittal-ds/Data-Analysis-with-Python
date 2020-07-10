#!/usr/bin/env python
# coding: utf-8

# The name, Jupyter, comes from the core supported programming languages that it supports: Julia, Python, and R. 
# 
# 

# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)

# The Pandas Library is a useful tool that enables us to read various datasets into a data frame; our Jupyter notebook platforms have a built-in Pandas Library so that all we need to do is import Pandas without installing.

# In[1]:


# The %... is an iPython thing, and is not part of the Python language.
# In this case we're just telling the plotting library to draw things on
# the notebook, instead of on a separate window.
get_ipython().run_line_magic('matplotlib', 'inline')
#this line above prepares IPython notebook for working with matplotlib

# See all the "as ..." contructs? They're just aliasing the package names.
# That way we can call methods like plt.plot() instead of matplotlib.pyplot.plot().

import numpy as np # imports a fast numerical programming library
import scipy as sp #imports stats functions, amongst other things
import matplotlib as mpl # this actually imports matplotlib
import matplotlib.cm as cm #allows us easy access to colormaps
import matplotlib.pyplot as plt #sets up plotting under plt
import pandas as pd #lets us handle data as dataframes
#sets up pandas table display
pd.set_option('display.width', 500)
pd.set_option('display.max_columns', 100)
pd.set_option('display.notebook_repr_html', True)
import seaborn as sns #sets up styles and gives us more plotting options


# Data Acquisition
# There are various formats for a dataset, .csv, .json, .xlsx etc. The dataset can be stored in different places, on your local machine or sometimes online.
# In this section, you will learn how to load a dataset into our Jupyter Notebook.
# In our case, the Automobile Dataset is an online source, and it is in CSV (comma separated value) format. Let's use this dataset as an example to practice data reading.
# 
# data source: https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data
# data type: csv
# 

# Read Data
# We use pandas.read_csv() function to read the csv file. In the bracket, we put the file path along with a quotation mark, so that pandas will read the file into a data frame from that address. The file path can be either an URL or your local file address.
# Because the data does not include headers, we can add an argument headers = None inside the read_csv() method, so that pandas will not automatically set the first row as a header.
# You can also assign the dataset to any variable you create.

# In[2]:


# Read the online file by the URL provides above, and assign it to variable "df"
other_path = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv"
df = pd.read_csv(other_path, header=None)


# ![image.png](attachment:image.png)

# After reading the dataset, we can use the dataframe.head(n) method to check the top n rows of the dataframe; where n is an integer. Contrary to dataframe.head(n), dataframe.tail(n) will show you the bottom n rows of the dataframe.

# In[3]:


# show the first 5 rows using dataframe.head() method
print("The first 5 rows of the dataframe") 
df.head(5)


# Question #1:
# check the bottom 10 rows of data frame "df".

# In[4]:


df.tail(10)


# Add Headers
# Take a look at our dataset; pandas automatically set the header by an integer from 0.
# To better describe our data we can introduce a header, this information is available at: https://archive.ics.uci.edu/ml/datasets/Automobile
# Thus, we have to add headers manually.
# Firstly, we create a list "headers" that include all column names in order. Then, we use dataframe.columns = headers to replace the headers by the list we created.

# In[5]:


# create headers list
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
print("headers\n", headers)


# We replace headers and recheck our data frame

# In[6]:


df.columns = headers
df.head(10)


# we can drop missing values along the column "price" as follows

# In[7]:


df.dropna(subset=["price"], axis=0)


# Question #2:
# Find the name of the columns of the dataframe

# In[8]:


print(df.columns)


# Save Dataset
# Correspondingly, Pandas enables us to save the dataset to csv by using the dataframe.to_csv() method, you can add the file path and name along with quotation marks in the brackets.
# 
# For example, if you would save the dataframe df as automobile.csv to your local machine, you may use the syntax below:

# In[9]:


df.to_csv("automobile.csv", index=False)


# This file got saved to following location:
# C:\Users\arpit

# We can also read and save other file formats, we can use similar functions to pd.read_csv() and df.to_csv() for other data formats, the functions are listed in the following table:

# ![image.png](attachment:image.png)

# Basic Insight of Dataset
# After reading data into Pandas dataframe, it is time for us to explore the dataset.
# There are several ways to obtain essential insights of the data to help us better understand our dataset.
# 
# Data Types
# Data has a variety of types.
# The main types stored in Pandas dataframes are object, float, int, bool and datetime64. In order to better learn about each attribute, it is always good for us to know the data type of each column. In Pandas:

# In[10]:


df.dtypes


# As a result, as shown above, it is clear to see that the data type of "symboling" and "curb-weight" are int64, "normalized-losses" is object, and "wheel-base" is float64, etc.

# ![image.png](attachment:image.png)

# Describe  
# If we would like to get a statistical summary of each column, such as count, column mean value, column standard deviation, etc. We use the describe method. This method will provide various summary statistics, excluding NaN (Not a Number) values.  

# In[11]:


df.describe()


# This shows the statistical summary of all numeric-typed (int, float) columns.
# For example, the attribute "symboling" has 205 counts, the mean value of this column is 0.83, the standard deviation is 1.25, the minimum value is -2, 25th percentile is 0, 50th percentile is 1, 75th percentile is 2, and the maximum value is 3.
# However, what if we would also like to check all the columns including those that are of type object.
# 
# You can add an argument include = "all" inside the bracket. Let's try it again.

# In[12]:


# describe all the columns in "df" 
df.describe(include = "all")


# Now, it provides the statistical summary of all the columns, including object-typed attributes.
# We can now see how many unique values, which is the top value and the frequency of top value in the object-typed columns.
# Some values in the table above show as "NaN", this is because those numbers are not available regarding a particular column type.

# Question #3:
# You can select the columns of a data frame by indicating the name of each column, for example, you can select the three columns as follows:
# dataframe[[' column 1 ',column 2', 'column 3']]
# 
# Where "column" is the name of the column, you can apply the method ".describe()" to get the statistics of those columns as follows:
# dataframe[[' column 1 ',column 2', 'column 3'] ].describe()
# 
# Apply the method to ".describe()" to the columns 'length' and 'compression-ratio'.

# In[13]:


df[ ['length', 'compression-ratio'] ].describe()


# Accessing Databases with Python

# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)

# Data Wrangling / Data Pre-processing

# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)

# In[ ]:




