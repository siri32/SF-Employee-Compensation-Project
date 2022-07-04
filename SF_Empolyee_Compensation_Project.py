#!/usr/bin/env python
# coding: utf-8

# # Introduction and Problem Statement
# 
# Be it a start-up or an established company, compensation is one of the most important things to maintain for the company in order to reward and retain it’s employees. A lot of start-ups are unsure whether they are paying their employees correctly.A compensation strategy is important for all organizations. It should be well structured and reasonable. From the San Francisco Employee Compensation Data set, we plan to visualize the pay structure in different organizations from 2013 till 2021. The major areas focused are the salary changes over years in San Francisco. It also focuses on how the salary differentiates from high rank and low rank employees and what are the benefits received by the high rank employees in some of the job families.
# 
# The San Francisco Employee Compensation Data consists of useful information from which valuable insights can be derived. Within the “Organization Group”, there are seven organizations in San Francisco. We will find out the most number of organization groups since 2013 and try to visualize change in those number of organization groups from 2013 to 2021. These organisations are divided into “Departments” which are primary organizational unit by city and county of San Francisco. These departments are further divided into “Job Families” and “Job types”. Job Families are the job fields of a particular major and Job Titles are the job roles within the families. The salaries, benefits and total compensation are the last columns in the data set from where we find the average salaries for Job families and Job type.
# 
# 

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


# Read DataSet
employ_df = pd.read_csv('employee-compensation.csv')
employ_df.head(10)


# In[4]:


#Information about the columns in the dataset.
employ_df.info()


# # Question1:
# What are the most number of organizations in San Francisco? How have the number of the organizations changed over years from 2013 to 2021?

# In[107]:


#To count the number of organization Groups from 2013 to 2022.
Organizationgroup_df = employ_df.groupby(['Organization Group']).agg('count').reset_index()
Organizationgroup_df = employ_df.groupby(['Organization Group']).size().reset_index(name ='Counts')
print(Organizationgroup_df)


# In[108]:


#To sort the count values in acending order
Organizationgroup_df = Organizationgroup_df.sort_values(by='Counts',ascending=False)
Organizationgroup_df


# In[124]:


#Bar graph plot on Organization Groups and counts  
figure = plt.figure(figsize=[15, 7])
plt.bar(data=Organizationgroup_df, x='Organization Group',height='Counts')
plt.xlabel(xlabel='OrganizationGroup', size=14)
plt.ylabel(ylabel='Counts', size=14)
plt.title(label='Count of values on organization', size=16)

plt.show()


# In[126]:


#To see increase in number of individual Organizations Groups from 2013 to 2022
OrganizationYear_df = employ_df.groupby(['Organization Group','Year']).agg('count').reset_index()
OrganizationYear_df = employ_df.groupby(['Organization Group','Year']).size().reset_index(name ='Counts')
print(OrganizationYear_df)


# In[127]:


#To sort the organizationGroup and year counts in descending order
OrganizationYear_df = OrganizationYear_df.sort_values(by='Counts',ascending=False)
OrganizationYear_df


# In[128]:


#Bar graph plot on Year and counts  
figure = plt.figure(figsize=[15, 7])
plt.bar(data=OrganizationYear_df, x='Year',height='Counts')
plt.xlabel(xlabel='Year', size=14)
plt.ylabel(ylabel='Counts', size=14)
plt.title(label='Count of values on years', size=16)

plt.show()


# # Conclusion
# 
# We can see from the above bar plot that public, works and transportation comes under the most number of organizations in San Francisco followed by community health. Culture and recreation comes under the least number of organizations. There are 28k organizational groups of public, works and transportation in 2021. Although most of these groups were increasing from 2013, 2020 sees a decrease in number of all groups from the previous years. It can be mainly due to the pandemic and is likely to increase coming forward.

# # Question2:
# 
# How are the Departments related to the Organizations and which are the most number of Departments under Organizations?
# 

# In[29]:


#Select data for year(2020)
employ_df1=employ_df[employ_df['Year']==2020]
employ_df1.tail(10)


# In[30]:



Departments_df = employ_df1.groupby(['Organization Group','Department']) ['Salaries'].agg('mean').reset_index()
Departments_df = employ_df1.groupby(['Organization Group','Department']).size().reset_index(name ='avgsal')
print(Departments_df)


# In[31]:


#To sort the organizationGroup and Department counts in descending order
Departments_df = Departments_df.sort_values(by='avgsal',ascending=False)
Departments_df


# In[35]:


#Pie plot on more number of departments
Departments_df.groupby(['Organization Group']).sum().plot(kind='pie', y='avgsal', autopct='%1.0f%%',
                                startangle=180, shadow=True, wedgeprops=dict(width=0.15),
                                title='Percentage of avg salary against year')


# #  Question3:
# 
# What is the change in average salaries over the years from 2013 to 2021?

# In[15]:


salary_df = employ_df.groupby(['Year']) ['Salaries'].agg('mean').reset_index()
salary_df = employ_df.groupby(['Year']).size().reset_index(name ='avg_year_sal')
print(salary_df)


# In[18]:


#Pie polt on avg_year_sal against year
salary_df.groupby(['Year']).sum().plot(kind='pie', y='avg_year_sal', autopct='%1.0f%%',
                                startangle=180, shadow=True, wedgeprops=dict(width=0.15),
                                title='Percentage of avg salary against year')


# #  Question4:
# 
# Show the Average Total Salaries of the top 10 and bottom 10 employees in 2 different types of Job Families?

# In[5]:


#Select data for JobFamily(Information Systems)
employ_df2=employ_df[employ_df['Job Family']=='Information Systems']
employ_df2.head(10)


# In[6]:


#Mean of total salary over Job = Information System
information_df = employ_df2.groupby(['Job']) ['Total Salary'].agg('mean').reset_index()
information_df = employ_df2.groupby(['Job']).size().reset_index(name ='avg_job_sal')
print(information_df)


# In[7]:


#To sort the organizationGroup and Department counts in descending order
information_df = information_df.sort_values(by='avg_job_sal',ascending=False)
information_df


# In[19]:


information_top_df=information_df.head(10)
information_top_df


# In[24]:


#Plot histogram for top 10 avg_job_sal
figure = plt.figure(figsize=[15, 7])
plt.hist(x=information_top_df, bins=10, alpha=0.6)
plt.xlabel(xlabel='Job', size=14)
plt.ylabel(ylabel='avg_job_sal', size=14)
plt.title(label='Avg salary against job', size=16)
plt.show()


# In[26]:


information_bottom_df=information_df.tail(10)
information_bottom_df


# In[27]:


#Plot histogram for bottom 10 avg_job_sal
figure = plt.figure(figsize=[15, 7])
plt.hist(x=information_bottom_df, bins=10, alpha=0.6)
plt.xlabel(xlabel='Job', size=14)
plt.ylabel(ylabel='avg_job_sal', size=14)
plt.title(label='Avg salary against job', size=16)
plt.show()


# # Question5:
# 
# How much does overtime cost the company? What is the maximum and the average value of the overtime money?

# In[35]:


#Mean and Max value of overtime against job family
jobfam_df = employ_df.groupby(['Job Family','Year']) ['Overtime'].agg(['mean','max'])
#print(jobfam_df)
#jobfam_df = employ_df.groupby(['Job Family','Year']).size().reset_index(name1 ='avg_overtime',name2 = 'max_overtime')
#jobfam_df = employ_df.groupby(['Job Family','Year']).size().reset_index(name ='max_overtime')
jobfam_df


# In[38]:


figure = plt.figure(figsize=[15, 7])
plt.boxplot(x=jobfam_df)
plt.xlabel(xlabel='Job Family', size=14)
plt.ylabel(ylabel='Year', size=14)
plt.title(label='Overtime data', size=16)

plt.show()

