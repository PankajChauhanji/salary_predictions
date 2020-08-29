import  scrapper as sc
import pandas as pd 
path = "C:/Users/pankaj/Documents/salary_prediction/chromedriver"
df = sc.get_jobs('software developer', 15, False, path, 15)