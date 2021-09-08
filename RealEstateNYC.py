#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 14:56:33 2020

@author: cassadygaier
"""

import pandas as pd
import datetime
import arff

data=pd.read_excel('CassRealestate.xlsx')
data=data.drop(columns=["Sold Price","Zipcode", "Last Asking Price","Listed Date","Status","Period","Year Built", "Year Renovated", "New Development"])
data=data.dropna()
data["Ownership"]= 0+(data["Ownership"]=='Condo')
data["Balcony/Terrace"]= 0
data["Private Outdoor"]= 0
H=(data["Outdoor Space"]== "Balcony") & (data["Outdoor Space"]== "Terrace")
data[H]=1
R=(data["Outdoor Space"]== "Garden") & (data["Outdoor Space"]== "Private Roof Access")
data[R]=1
data['Allow pets']=0
data['Allow Washer/Dryer']=0
data['Allow Financing']=0
for i in data.index:
    if 'Pets' in data['Building Allows'][i]:
        data['Allow pets'][i]=1
    if 'Washer/Dryer' in data['Building Allows'][i]:
        data['Allow Washer/Dryer'][i]=1
    if 'Financing' in data['Building Allows'][i]:
        data['Allow Financing'][i]=1
data1=data[data['Updated Date']<datetime.datetime.strptime('02/29/2020',"%m/%d/%Y")]
data2=data[data['Updated Date']>datetime.datetime.strptime('04/1/2020',"%m/%d/%Y")]

#data1=pd.read_csv("data1.csv")
K=data1["Parking"]!=0
data1["Parking"][K]=1
#data2=pd.read_csv("data2.csv")
B=data2["Parking"]!=1
data2["Parking"][B]=1
F=data1["Attended Lobby"]=="Unattended Lobby"
data1["Attended Lobby"][F]=0
G=((data1["Attended Lobby"]!=1)&(data1["Attended Lobby"]!=1))
data1["Attended Lobby"][G]=1
#data2=pd.read_csv("data2.csv")
V=((data2["Attended Lobby"]!=1)&(data2["Attended Lobby"]!=0))
data2["Attended Lobby"][V]=1
Y=data2["Attended Lobby"]=="Unattended Lobby"
data2["Attended Lobby"][Y]=0
        
data1.to_csv('data1.csv',index=False)
data2.to_csv('data2.csv',index=False)


data1=data1.rename(lambda x:x.replace(' ','_'),axis='columns') #replacing spaces in column header with _ for weka
data2=data2.rename(lambda x:x.replace(' ','_'),axis='columns')


for i in data1:
    if data1.dtypes[i]=='object':
        print(i+' is removed.')
        data1=data1.drop([i],axis=1)
for i in data2:
    if data2.dtypes[i]=='object':
        print(i+' is removed.')
        data2=data2.drop([i],axis=1)  
arff.dump('data2firstexperiment.arff'
      , data2.values
      , relation='name'
      , names=data2.columns)        
arff.dump('data1firstexperiment.arff'
      , data1.values
      , relation='name'
      , names=data1.columns)




