"""
step1: scrapp the data from web using selenium.
step2: save that data as csv file.
"""
import data_scrapper as ds 
import pandas as pd 

path = "C:/Users/pankaj/Documents/salary_prediction/chromedriver"

df = ds.get_jobs('data scientist',10, False, path, 15)

df.to_csv('Datafile.csv', index = False)