# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 16:12:09 2020

@author: pankaj
"""

import pandas as pd
df = pd.read_csv('data_file1.csv')

#   Some salary are in per hour  also employer provided so lets make another columns for them 
df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['employer_provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)

#   First remove all those rows where salary is not present.
df = df[df['Salary Estimate']!='-1']

#   lets remove the $ from salaries.
#   For that first lets split salary column.
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
#   Now remove the $ and k sign
salary2  = salary.apply(lambda x: x.replace('K', '').replace('$', ''))

#   replace per hour and emploer provided now.
salary3 = salary2.apply(lambda x: x.lower().replace('per hour','').replace('employer provided salary:',''))

#   Now lets find average of min and max salary and add it to main data file.
df['min_salary'] = salary3.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = salary3.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary+df.max_salary)/2

#   Company name is having rating so lets remove that also.
df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] <0 else x['Company Name'][:-3], axis = 1)

#add the location as state in data
df['job_state'] = df['Location'].apply(lambda x: x.split(',')[1])
df.job_state.value_counts()

df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis = 1)

# Lets make anothre colomns for age of the company.
df['age'] = df.Founded.apply(lambda x: x if x <1 else 2020 - x)


#   Lets make another colomns for the most demanded technology here.
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df['hadoop'] = df['Job Description'].apply(lambda x: 1 if 'hadoop' in x.lower() else 0)
df['tableau'] = df['Job Description'].apply(lambda x: 1 if 'tableau' in x.lower() else 0)
df['mongo'] = df['Job Description'].apply(lambda x: 1 if 'mongo' in x.lower() else 0)
df['R_studio'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)
df.R_studio.value_counts()
df['spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df.spark.value_counts()
df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df.aws.value_counts()
df['excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
df.excel.value_counts()

#   Drop the first colomns because its of no use.
df.columns         #  get col name

df2 = df.drop(['Unnamed: 0'], axis =1)

#   Lets save this final file.
df2.to_csv('data_file_cleaned.csv',index = False)
