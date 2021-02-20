#!/usr/bin/env python
# coding: utf-8

# # Extract Data from SQL Database (Postgresql) in Pandas
# Bonus question to investigate if the employee data is fake through data visualizations.
# 

# In[1]:


get_ipython().system('pip3 install psycopg2-binary')


# In[5]:


import pandas as pd
from sqlalchemy import create_engine
from server import server

# server has my postgresql username and password path in a separate file called server.py
# I kept my username and password separate from the submission of homework.

engine = create_engine(server)
connection = engine.connect()
salaries_df = pd.read_sql('SELECT * FROM salaries', connection)


# In[6]:


salaries_df.head()


# In[8]:


engine = create_engine(server)
connection = engine.connect()
titles_df = pd.read_sql('SELECT * FROM titles', connection)


# In[9]:


titles_df.head()


# In[10]:


engine = create_engine(server)
conneciton = engine.connect()
employees_df = pd.read_sql('SELECT * FROM employees', connection)


# In[11]:


employees_df.head()


# In[20]:


renamed_employees_df = employees_df.rename(columns={'emp_title_id':'title_id'})
renamed_employees_df


# ## Merge the Three Tables

# In[22]:


test_df = pd.merge(salaries_df, renamed_employees_df[['emp_no','title_id']], on='emp_no', how='left')
test_df


# In[25]:


merged_df = pd.merge(test_df, titles_df[['title_id', 'title']], on="title_id", how="left")
merged_df


# ## Create a histogram to visualize the most common salary ranges for employees

# In[28]:


import matplotlib.pyplot as plt

merged_df.hist(column='salary')
plt.title("Frequency of Salary of Pewlett Hackard Employees")
plt.xlabel("Salary")
plt.ylabel("Frequency")


# In[31]:


# Another way to find out the most common salary of employees. Figure out the mode.

merged_df.mode()['salary'][0]


# ## Create a bar chart of average salary by title

# In[33]:


merged_df.groupby('title')['salary'].mean()


# In[44]:


avg_salary_title_chart = merged_df.groupby('title')['salary'].mean()
avg_salary_title_chart.plot(kind="bar", figsize=(8,6))
plt.xlabel('Staff Title')
plt.ylabel('Average Salary')
plt.title('Average Salary by Pewlett Hackard Staff Title')
plt.tight_layout()
plt.show()


# In[45]:


# Exploring the data for fun
merged_df.groupby('title')['salary'].count()

