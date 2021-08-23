# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 21:08:39 2021

@author: Melvin Wayne Abraham | Module 6_Python Assignment
"""

#Question 1: Removed currency label from excel file
#Write a program to read total profit of all months and show it using a line plot.
#Use the total profit data provided for each month. The generated line plot must include the following properties:
#X label name = Month Number
#Y label name = Total Profit

#Load the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

#Use a different style
style.use('bmh')

#Import the csv file, create a dataframe and replace currency sybmols
df = pd.read_csv("buad5802-m6-python-assignment-data-file.csv")
profitList = df ['Profit']
profitList = profitList.str.replace(',', '')
profitList = profitList.apply(lambda x: x.replace ('$', ''))
#print(profitList)
profitList = profitList.tolist() #Convert values to a list

str_to_float = [] #Initialize an empty list

#Create a for loop and append each item in the Profit List
for item in profitList:

    str_to_float.append(float(item))
#print(str_to_float)
profitList = str_to_float

#Create a second dataframe and convert it over to a list
monthList  = df ['Month#'].tolist()

#Create a plot with the months on the x-axis and profits on the y-axis
plt.plot(monthList, profitList, marker='v', markerfacecolor='k', color='orange', linewidth=2)
plt.xlabel('Month Number')
plt.ylabel('Total Profit')
plt.xticks(monthList)
plt.title('Company Profits')
plt.yticks(np.arange(start=140000, stop=220000, step=25000 )) #Start at 140,000 instead of zero and step up every 25,000
plt.show()


#Question 2:
#Write a program to get total profit of all months and to show a line plot with the following style properties:
#Line style should be dotted
#Line color should be red
#Add a circle marker
#Line marker color should be red
#Line width should be 3
#Show the legend at the lower right
#X label name = Month Number
#Y label name = Total Profit

#Load the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Import the csv file, create a dataframe and replace currency sybmols
df = pd.read_csv("buad5802-m6-python-assignment-data-file.csv")
profitList = df ['Profit']
profitList = profitList.str.replace(',', '')
profitList = profitList.apply(lambda x: x.replace ('$', ''))
#print(profitList)
profitList = profitList.tolist() #Convert values to a list

str_to_float = []#Initialize an empty list

#Create a for loop and append each item in the Profit List
for item in profitList:

    str_to_float.append(float(item))
#print(str_to_float)
profitList = str_to_float
monthList  = df ['Month#'].tolist()

#Create a plot with the months on the x-axis and profits on the y-axis
plt.plot(monthList, profitList, label = 'Monthly Profits', 
      color='r', marker='o', markerfacecolor='k', 
      linestyle='--', linewidth=3)
      
plt.xlabel('Month Number')
plt.ylabel('Total Profit')
plt.legend(loc='lower right')
plt.xticks(monthList)
plt.title('Company Annual Sales')
plt.yticks(np.arange(start=140000, stop=220000, step=25000 )) #Start at 140,000 instead of zero and step up every 25,000
plt.show()

#Question 3:
#Write a program to read all product sales data and to show it using a multiline plot.
#Display the number of units sold per month for each product, using multiline points 
#(i.e., separate plotline for each product).

#Load the libraries
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

#Use a different style
style.use('seaborn-pastel')

#Import the csv file, create multiple dataframes for each item
df = pd.read_csv("buad5802-m6-python-assignment-data-file.csv")
monthList  = df ['Month#'].tolist()
Face_Cream   = df ['Face_Cream'].tolist()
Face_Wash   = df ['Face_Wash'].tolist()
Toothpaste = df ['Toothpaste'].tolist()
Bath_Soap   = df ['Bath_Soap'].tolist()
Shampoo   = df ['Shampoo'].tolist()
Moisturizer = df ['Moisturizer'].tolist()

#Create a plot with the months on the x-axis and number of units sold on the y-axis
#First make the graph and then change order of the legend so it matches highest to lowest
plt.plot(monthList, Bath_Soap, label = 'Bath Soap', marker='o', linewidth=1)
plt.plot(monthList, Toothpaste, label = 'ToothPaste', marker='o', linewidth=1)
plt.plot(monthList, Face_Cream,   label = 'Face Cream', marker='o', linewidth=1)
plt.plot(monthList, Shampoo, label = 'Shampoo', marker='o', linewidth=1)
plt.plot(monthList, Face_Wash,   label = 'Face Wash',  marker='o', linewidth=1)
plt.plot(monthList, Moisturizer, label = 'Moisturizer', marker='o', linewidth=1)

#Create labels for x&y axis, legend and arrange dataset
plt.xlabel('Month Number')
plt.ylabel('# of Units Sold')
plt.legend(loc='upper right', prop={'size': 8})
plt.xticks(monthList)
plt.yticks(np.arange(start=0, stop=18500, step=1500 ))
#plt.yticks([1000, 2000, 4000, 6000, 8000, 10000, 12000, 15000, 18000])
plt.title('Product Sales Data')
plt.show()

#Question 4:
#Write a program to read bathing soap face wash of all months and to display it using the subplot.

#Load the libraries
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

#Use a different style
style.use('seaborn')

#Import the csv file, create multiple dataframes for the months, bathing soap and face wash
df = pd.read_csv("buad5802-m6-python-assignment-data-file.csv")
monthList  = df ['Month#'].tolist()
Bath_Soap   = df ['Bath_Soap'].tolist()
Face_Wash   = df ['Face_Wash'].tolist()

#Create subplots and unpack variables with two items in one graph separately
fig, ax = plt.subplots(2, sharex=True)
ax[0].plot(monthList, Bath_Soap, label = 'Bath Soap', color='c', marker='D', markerfacecolor='k', linewidth=2)
ax[0].set_title('Bath Soap Sales')
ax[1].plot(monthList, Face_Wash, label = 'Face Wash', color='m', marker='h', markerfacecolor = 'k',linewidth=1)
ax[1].set_title('Face Wash Sales')

#Create tickmarks and labels
plt.xticks(monthList)
plt.xlabel('Month Number')
plt.ylabel('# of Units Sold', loc='center')
plt.show()

