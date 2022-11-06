from selenium import webdriver
import time 
import pandas as pd 
import urllib.request

data=pd.read_csv('API_SH.DYN.2024_DS2_en_csv_v2_4543808.csv',sep=',')
new_data=data.dropna(axis=1,how='all')
data_csv=new_data.to_csv('hiv.csv')

#try:
# rising_cases=[]
# for column in new_data.columns.values:
#     if new_data.columns.values['2020']>new_data.columns.values['2019'] and new_data.columns.values['2020']>new_data.columns.values['2018']:
#         rising_cases.append(column)
#         print(rising_cases)
    
# # except:
# #     print("couldn't extract data")

