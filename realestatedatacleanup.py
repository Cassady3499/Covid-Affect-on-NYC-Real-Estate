#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 19:24:07 2020

@author: cassadygaier
"""


import pandas as pd
import datetime

data=pd.read_excel('CassRealestate.xlsx')
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
data["Balcony/Terrace"]= 0
data["Private Outdoor"]= 0
H=(data["Outdoor Space"]== "Balcony") | (data["Outdoor Space"]== "Terrace")
data["Balcony/Terrace"][H]=1
R=(data["Outdoor Space"]== "Garden") | (data["Outdoor Space"]== "Private Roof Access")
data["Private Outdoor"][R]=1

K=data["Parking"]!=0
data["Parking"][K]=1

F=data["Attended Lobby"]=="Unattended Lobby"
data["Attended Lobby"][F]=0
G=((data["Attended Lobby"]!=1)&(data["Attended Lobby"]!=0))
data["Attended Lobby"][G]=1


data=data.drop(["Building Allows","Has Wash Dryer","Allows Pets", "Building Does Not Allow","New Development"],axis=1)
data1=data[data['Updated Date']<datetime.datetime.strptime('02/29/2020',"%m/%d/%Y")]
data2=data[data['Updated Date']>datetime.datetime.strptime('04/1/2020',"%m/%d/%Y")]



data1.to_csv('data1.csv')
data2.to_csv('data2.csv')
