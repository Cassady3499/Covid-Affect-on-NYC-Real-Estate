#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 14:37:47 2020

@author: cassadygaier
"""
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from sklearn.naive_bayes import GaussianNB #this implements the Naive Bayes Gaussian algorithm


data1=pd.read_csv('data1.csv') #training & test data
data2=pd.read_csv('data2.csv') #test data
#data1['allow pets']=pd.to_numeric(data1['allow pets'])
data1=data1.drop(columns=["Original Price", "$/Sqft", "$/Room"]) #this was removed from the dataset it made the prediction to accurate, since we wanted to predict the affect without the pandemic, we needed to remove features related to it
data2=data2.drop(columns=["Original Price", "$/Sqft", "$/Room"])
data2copy=data2.copy()
data2['Updated Date'] = pd.to_datetime(data2['Updated Date']).dt.strftime('%m-%d-%Y')

data1=data1.drop([],axis=1)
for i in data2copy: #lines 24-25, this loop drops the category features/discrete features, we do this because it guassian naive bayes regression, meaning it only takes numeric features
    if data2copy.dtypes[i]=='object': #object means category features
        print(i+' is removed.') # this creates the algorithm engine, it prepares for the aglorithm, this preparation is for line 36
        data2copy=data2copy.drop([i],axis=1)
for i in data2:
    if data2.dtypes[i]=='object':
        print(i+' is removed.')        
        data2=data2.drop([i],axis=1)
for i in data1:
    if data1.dtypes[i]=='object': #this judges to see if it is numeric or not, 
        print(i+' is removed.') #
        data1=data1.drop([i],axis=1)
mnb = GaussianNB()  # this creates the algorithm engine and the framework for it to run, so it gets ready fo the data to be filled in and trained, which is all done in the gaussian library, here we just call the function

data1['Price']=data1['Price'].astype(int) #this changes the data type from float to integer, this is becuase the naive bayes gauassion regression algo can't run the float data type, but it can run the integer data type
mnb.fit(data1.drop(['Price'],axis=1),data1['Price']) #This is the beginning and the end of the training process, since gausssianNB library has the code already, it just needs to be ran 

data1["predictedprice"]=mnb.predict(data1.drop(columns=['Price'])) #This the prediction process on data1, technically called the "test process", since it is doing prediction
data2["predictedprice"]=mnb.predict(data2copy.drop(columns=['Price'])) #This the prediction process on data2, technically called the "test process", since it is doing prediction
#data1["sqaure error"]= (data1["predictedprice"]-data1["Price"])* (data1["predictedprice"]-data1["Price"]) #square error for during covid
#data2["sqaure error"]= (data2["predictedprice"]-data2["Price"])* (data2["predictedprice"]-data2["Price"]) #square error for during covid

data1["sqaure error"]= (data1["predictedprice"]-data1["Price"])* (data1["predictedprice"]-data1["Price"])  #square error for during covid")
data2["sqaure error"]= (data2["predictedprice"]-data2["Price"])* (data2["predictedprice"]-data2["Price"])  #square error for pre-covd")
print(str(data1["sqaure error"].mean())+"  Sqaure error for during covid")
print(str(data2["sqaure error"].mean())+ "  Sqaure error for pre covid")



data2["difference"]= (data2["predictedprice"]-data2["Price"])/data2["Price"]*100 #difference between price and predicted for during covid
data1["difference"]= (data1["predictedprice"]-data1["Price"])/data1["Price"]*100 #average difference between price and predict for prevoidf
print(data1["difference"].mean()) #Precovid difference
print(data2["difference"].mean()) #during covid difference

#plt.scatter(data2[data2["Price"]>300000]["Price"],data2[data2["Price"]>300000]["predictedprice"], c="blue",s=1,linewidths = 1, marker= "o", edgecolor = "blue", label="During-Covid")
#plt.scatter(data1[data1["Price"]>300000]["Price"],data1[data1["Price"]>300000]["predictedprice"], c="red",s=1,linewidths = 1, marker= "x", edgecolor = "red", label="Pre-Covid")

#plt.scatter(data2[data2['predictedprice']>300000]["Price"],data2[data2['predictedprice']>300000]["predictedprice"], c="red",s=1,linewidths = 1, marker= "o", edgecolor = "red", label="During Covid")
plt.scatter(data1[data1['predictedprice']>300000]["Price"],data1[data1['predictedprice']>300000]["predictedprice"], c="blue",s=1,linewidths = 1, marker= "x", edgecolor = "blue", label="Pre Covid")


#plt.scatter(data[data['predictedprice']>300000]["Price"],data[data['predictedprice']>300000]["predictedprice"], c="red",s=1,linewidths = 1, marker= "o", edgecolor = "red", label="During Covid")
#plt.scatter(data1[data1['predictedprice']>300000]["Price"],data1[data1['predictedprice']>300000]["predictedprice"], c="blue",s=1,linewidths = 1, marker= "x", edgecolor = "blue", label="Pre Covid")


ax=plt.gca()
lims = [
    np.min([ax.get_xlim(), ax.get_ylim()]),  # min of both axes
    np.max([ax.get_xlim(), ax.get_ylim()]),  # max of both axes
]

# plot y=x line
ax.plot(lims, lims, 'k-', alpha=0.75, zorder=0)


ticks_x = ticker.FuncFormatter(lambda x, pos: '{0:g} M'.format(x/1000000))
ax.xaxis.set_major_formatter(ticks_x)
ticks_y = ticker.FuncFormatter(lambda x, pos: '{0:g} M'.format(x/1000000))
ax.yaxis.set_major_formatter(ticks_y)

plt.xlabel("Actual Price") #x-axis label
plt.ylabel("Predicted-Price") #y-axis label
plt.legend()


print(str(data1["Price"].mean())+ "  The is the average real price of Condos&Coops Precovid1")
print(str(data2["Price"].mean())+ "  The is the average real price of Condos&Coops during2")
print(str(data1["predictedprice"].mean())+ "  The is the average predicted price of Condos&Coops Precovid3")
print(str(data2["predictedprice"].mean())+ "  The is the average predicted price of Condos&Coops during4")





print(data1["Price"].median())
print(data2["Price"].median())
print(str(data1["sqaure error"].mean())+" This is mean sqaure error for data1, pre-covid") #this is converting the number (mean sqaure error) into string, so they can be combined
print(str(data2["sqaure error"].mean())+" This is mean sqaure error for data2, during-covid")
print(str((data2["Price"].mean()-data1["Price"].mean())/data2["Price"].mean()*100)+ "This is the change (decrease) in Condo&Coop's for the selected areas")

