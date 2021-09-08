#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 16:33:46 2020
@author: cassadygaier
"""
import pandas as pd
import numpy as np
#import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
#import mglearn
#mglearn.plots.plot_knn_regression(n_neighbors=1)
from sklearn.neighbors import KNeighborsRegressor

data1=pd.read_csv('data1.csv')
data2=pd.read_csv('data2.csv')
#data1['allow pets']=pd.to_numeric(data1['allow pets'])
data1=data1.drop(columns=["Original Price", "$/Sqft", "$/Room"])
data2=data2.drop(columns=["Original Price", "$/Sqft", "$/Room"])
data2copy=data2.copy()
data2['Updated Date'] = pd.to_datetime(data2['Updated Date']).dt.strftime('%m-%d-%Y')

#data1=data1.drop([],axis=1)
for i in data2copy:
    if data2copy.dtypes[i]=='object':
        print(i+' is removed.')
        data2copy=data2copy.drop([i],axis=1)
#for i in data2:
#    if data2.dtypes[i]=='object':
#        print(i+' is removed.')        
#        data2=data2.drop([i],axis=1)
for i in data1:
    if data1.dtypes[i]=='object':
        print(i+' is removed.')
        data1=data1.drop([i],axis=1)
neigh = KNeighborsRegressor ()
#neigh.fit(data1.drop(columns=['Price']),data1['Price']) #Knearest neighbor for data1 pre-covid
neigh.fit(data2copy.drop(columns=['Price']),data2copy['Price'])
print(neigh.predict(data2copy.drop(columns=['Price'])))

data2["predictedprice"]=neigh.predict(data2copy.drop(columns=['Price']))
data1["predictedprice"]=neigh.predict(data1.drop(columns=['Price']))

data1["sqaure error"]= (data1["predictedprice"]-data1["Price"])* (data1["predictedprice"]-data1["Price"])#sqaure error
data2["sqaure error"]= (data2["predictedprice"]-data2["Price"])* (data2["predictedprice"]-data2["Price"])#sqaure error

print(str(data2["sqaure error"].mean())+"  Sqaure error for during covid")
print(str(data1["sqaure error"].mean())+ "  Sqaure error for pre covid")

data2["difference"]= (data2["predictedprice"]-data2["Price"])/data2["Price"]*100 #difference between price and predicted
#data1["difference"]= (data1["predictedprice"]-data1["Price"])/data1["Price"]*100

print(data1["sqaure error"].mean())#using pre-covid data to predict difference
print(data2["sqaure error"].mean())# using during covid data to predict difference
print(str((data2[data2['Ownership']== 1])[["Ownership","Price","predictedprice","Bedrooms","difference"]])+ "Condos1") 
print(str((data2[data2['Ownership']== 0])[["Ownership","Price","predictedprice","Bedrooms","difference"]])+ "Coops0")
print((data2[data2['Bedrooms']==4])[["Price","predictedprice","Bedrooms","difference"]])
print("the mean of owership with coops: ")
print((((data2[data2['Bedrooms']== 4]['predictedprice']-data2[data2['Bedrooms']== 4]['Price'])/data2[data2['Bedrooms']== 4]['Price'])*100).mean())#difference betwen price and predicted price for condos and coops
print("the mean of owership with condos: ")
print((((data2[data2['Ownership']== 1]['predictedprice']-data2[data2['Ownership']== 1]['Price'])/data2[data2['Ownership']== 1]['Price'])*100).mean())# Condos
print((((data1[data1['Ownership']== 1]['predictedprice']-data1[data1['Ownership']== 1]['Price'])/data2[data2['Ownership']== 1]['Price'])*100).mean())# Condos
print((((data2[data2['Ownership']== 0]['predictedprice']-data2[data2['Ownership']== 0]['Price'])/data2[data2['Ownership']== 0]['Price'])*100).mean())# Cooops
print((((data2[data1['Ownership']== 0]['predictedprice']-data2[data2['Ownership']== 0]['Price'])/data2[data2['Ownership']== 0]['Price'])*100).mean())# Cooops


print((((data2[data2['Neighborhood']=='Greenwich Village (GV)']['predictedprice']-data2[data2['Neighborhood']=='Greenwich Village (GV)']['Price'])/data2[data2['Neighborhood']=='Greenwich Village (GV)']['Price'])*100).mean())

plt.scatter(data1[data1["Price"]>300000]["Price"],data1[data1["Price"]>300000]["predictedprice"], c="blue",s=1,linewidths = 1, marker= "o", edgecolor = "blue", label="Pre-Covid")
plt.scatter(data2[data2["Price"]>300000]["Price"],data2[data2["Price"]>300000]["predictedprice"], c="red",s=1,linewidths = 1, marker= "x", edgecolor = "red", label="During-Covid")
#plt.scatter(data2[(data2["Price"]>300000)&(data2["Ownership"]== 1)]["Price"],data2[(data2["Price"]>300000)&(data2["Ownership"]== 1)]["predictedprice"], c="green",s=1,linewidths = 1, marker= "o", edgecolor = "green", label="Condo")
#plt.scatter(data2[(data2["Price"]>300000)&(data2["Ownership"]== 0)]["Price"],data2[(data2["Price"]>300000)&(data2["Ownership"]== 0)]["predictedprice"], c="red",s=1,linewidths = 1, marker= "x", edgecolor = "red", label="Coop")

plt.scatter(data1[data1["Price"]>300000]["Price"],data1[data1["Price"]>300000]["predictedprice"], c="blue",s=1,linewidths = 1, marker= "o", edgecolor = "blue", label="Pre-Covid")
plt.scatter(data2[data2["Price"]>300000]["Price"],data2[data2["Price"]>300000]["predictedprice"], c="red",s=1,linewidths = 1, marker= "x", edgecolor = "red", label="During-Covid")

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

lt.xlabel("Pre-Covid Prices") #x-axis label
plt.ylabel("During-Covid Prices") #y-axis label
plt.legend()
print(data1["sqaure error"].mean())#using pre-covid data to predict difference
print(data2["sqaure error"].mean())# using during covid data to predict difference

"""
print('4 bedrooms:          ',end='')
print((((data2[data2['Bedrooms']== 4]['predictedprice']-data2[data2['Bedrooms']== 4]['Price'])/data2[data2['Bedrooms']== 4]['Price'])*100).mean())#dPrice difference of 4bedrooms
print('3 bedrooms:          ',end='')
print((((data2[data2['Bedrooms']== 3]['predictedprice']-data2[data2['Bedrooms']== 3]['Price'])/data2[data2['Bedrooms']== 3]['Price'])*100).mean())#Price difference of 3bedroom
print('2 bedrooms:          ',end='')
print((((data2[data2['Bedrooms']== 2]['predictedprice']-data2[data2['Bedrooms']== 2]['Price'])/data2[data2['Bedrooms']== 2]['Price'])*100).mean())#Price difference of 3bedroom
print('1 bedrooms:          ',end='')
print((((data2[data2['Bedrooms']== 1]['predictedprice']-data2[data2['Bedrooms']== 1]['Price'])/data2[data2['Bedrooms']== 1]['Price'])*100).mean())#Price difference of 3bedroom



"""
print(str(data1['Price'].mean())+ "  This is the average price for a 1 bedroom Condo/Coop Pre Covid")

print('4 bedrooms:          ',end='')
print((((data1[data1['Bedrooms']== 4]['predictedprice']-data1[data1['Bedrooms']== 4]['Price'])/data1[data1['Bedrooms']== 4]['Price'])*100).mean())#dPrice difference of 4bedrooms
print('3 bedrooms:          ',end='')
print((((data1[data1['Bedrooms']== 3]['predictedprice']-data1[data1['Bedrooms']== 3]['Price'])/data1[data1['Bedrooms']== 3]['Price'])*100).mean())#Price difference of 3bedroom
print('2 bedrooms:          ',end='')
print((((data1[data1['Bedrooms']== 2]['predictedprice']-data1[data1['Bedrooms']== 2]['Price'])/data1[data1['Bedrooms']== 2]['Price'])*100).mean())#Price difference of 3bedroom
print('1 bedrooms:          ',end='')
print((((data1[data1['Bedrooms']== 1]['predictedprice']-data1[data1['Bedrooms']== 1]['Price'])/data2[data2['Bedrooms']== 1]['Price'])*100).mean())#Price difference of 3bedroom

print(str(data1['Price'].mean())+ "  This is the average price for a 1 bedroom Condo/Coop Pre Covid")



print(str(data1["Price"].mean())+ "  The is the average real price of Condos&Coops Precovid1")
print(str(data2["Price"].mean())+ "  The is the average real price of Condos&Coops during2")
print(str(data1["predictedprice"].mean())+ "  The is the average predicted price of Condos&Coops Precovid3")
print(str(data2["predictedprice"].mean())+ "  The is the average predicted price of Condos&Coops during4")

print(data1["Price"].median())
print(data2["Price"].median())

print(str((data2["Price"].mean()-data1["Price"].mean())/data2["Price"].mean()*100)+ "This is the change (decrease) in Condo&Coop's for the selected areas")
