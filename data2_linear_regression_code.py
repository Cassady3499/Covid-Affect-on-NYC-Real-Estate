#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 14:13:29 2020

@author: cassadygaier
"""
import numpy
from math import ceil
import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

pd.set_option('display.max_rows',None)

data=pd.read_csv('data2.csv')
data1=pd.read_csv('data1.csv')
#data["predictedprice"]=4089.415  * data['Zipcode'] +21684.0077 * data['Rooms'] +15004.0681 * data['Bedrooms'] +33586.6762 * data['Bathrooms'] +41.7114 * data['Approx SqFt']  -68.7508 * data['DOM'] +0.0103 * data['Original Price'] +   0.8063 * data['Last Asking Price'] +57.3594 * data['Maint/CC'] -202.1939 * data['# Units'] +2656.4463 * data['# Floors'] -40957809.6198
data["predictedprice"]=781822.5864 * data['Bathrooms'] + 802.2119* data['Approx SqFt']+1375.1264* data['DOM'] + 573.622 * data['Maint/CC'] -1154784.0878
data["difference"]= (data["predictedprice"]-data["Price"])/data["Price"]*100 #predicted price differennce, average difference between price and predictprice for during covid
data1["predictedprice"]=781822.5864 * data1['Bathrooms'] + 802.2119* data1['Approx SqFt']+1375.1264* data1['DOM'] + 573.622 * data1['Maint/CC'] -1154784.0878
data1["difference"]= (data1["predictedprice"]-data1["Price"])/data1["Price"]*100 #average difference between price and predict for pre-covid

data["sqaure error"]= (data["predictedprice"]-data["Price"])* (data["predictedprice"]-data["Price"])  #square error for during covid")
data1["sqaure error"]= (data1["predictedprice"]-data1["Price"])* (data1["predictedprice"]-data1["Price"])  #square error for pre-covd")
print(str(data["sqaure error"].mean())+"  Sqaure error for during covid")
print(str(data1["sqaure error"].mean())+ "  Sqaure error for pre covid")
#print(str(data1["average price"].mean())+ "The is the average price of Condos&Coops Precovid")

pd.set_option('display.max_columns',None)
data['Updated Date'] = pd.to_datetime(data['Updated Date'])#.dt.strftime('%m-%d-%Y')

#print(data[['Updated Date',"predictedprice",'Price','difference','Address','Unit']])
#print(data1[['Updated Date',"predictedprice",'Price','difference','Address','Unit']])

#data.plot.scatter('Updated Date','Price')
#matplotlib.pyplot.scatter("Updated Date".data, "Price","predictedprice")

#plt.xlabel("Updated Date") #x-axis label
#plt.ylabel("Apartment Prices") #y-axis label
#plt.title()
#plt.scatter(data["Updated Date"],data["predictedprice"], c="green",linewidths = 2, marker= "x", edgecolor = "green")
#plt.scatter(data["Price"],data["predictedprice"], c="red",s=1,linewidths = 1, marker= "o", edgecolor = "red", label="During Covid")
#plt.scatter(data1["Price"],data1["predictedprice"], c="blue",s=1,linewidths = 1, marker= "x", edgecolor = "blue", label="Pre Covid")

plt.scatter(data[data['predictedprice']>300000]["Price"],data[data['predictedprice']>300000]["predictedprice"], c="red",s=1,linewidths = 1, marker= "o", edgecolor = "red", label="During Covid")
plt.scatter(data1[data1['predictedprice']>300000]["Price"],data1[data1['predictedprice']>300000]["predictedprice"], c="blue",s=1,linewidths = 1, marker= "x", edgecolor = "blue", label="Pre Covid")



#plt.axis([0,20])
#plt.polyfit(data["Updated Date"],data["difference"], c="blue", marker= "o")
plt.xlabel("Actual Price") #x-axis label
plt.ylabel("Predicted-Price") #y-axis label
plt.legend()
#plt.scatter(data["Updated Date"]=="green",linewidths = 2, marker= "x", edgecolor = "green")
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

#ax.ticklabel_format(useOffset=False, style='plain')
#plt.locator_params(axis='x', nbins=10)

plt.show()
print(str(data1["sqaure error"].mean())+" This is mean sqaure error for data1, pre-covid") #this is converting the number (mean sqaure error) into string, so they can be combined
print(str(data["sqaure error"].mean())+" This is mean sqaure error for data, during-covid")
print(data["Price"].median())
print(data1["Price"].median())
print(str(data["difference"].mean())+ "Difference between real Price and predicted with During Covid")
print(str(data1["difference"].mean())+ "Difference between real Price and predicted with PreCovid")
#plt.scatter(data['Updated Date'],data[['Price','predictedprice']])
#plt.scatter(data["Updated Date"],data["predictedprice"], c="green",linewidths = 2, marker= "x", edgecolor = "green")

#plt.setp(data['Updated Date'][::3], rotation=45, ha="right")
#plt.show()
#plt.xticks(range(data['Updated Date'].shape[0])[::8],data['Updated Date'][::8])

print(str(data1["Price"].mean())+ "  The is the average real price of Condos&Coops Precovid1")
print(str(data["Price"].mean())+ "  The is the average real price of Condos&Coops during2")
print(str(data1["predictedprice"].mean())+ "  The is the average predicted price of Condos&Coops Precovid3")
print(str(data["predictedprice"].mean())+ "  The is the average predicted price of Condos&Coops during4")





print(str((data["Price"].mean()-data1["Price"].mean())/data["Price"].mean()*100)+ "This is the change (decrease) in Condo&Coop's for the selected areas")  
