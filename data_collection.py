from selenium import webdriver
import time 
import pandas as pd 
import urllib.request

data=pd.read_csv('API_SH.DYN.2024_DS2_en_csv_v2_4543808.csv',sep=',')
new_data=data.dropna(axis=1,how='all')
print(new_data)
