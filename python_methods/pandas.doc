Pandas docs link: http://pandas.pydata.org/docs/

Use of Pandas?

1. Super helpful to anlysis the complex form of tabular files.

Pandas is not inbuilt library to make use of it. Need to install it by using a short cut on Pycharm:

"import pandas" > click red bulb symbol > install pandas packages > 

##it installs autometically all the pandas packages.

ex:

weather_data.csv

day,temp,condition
Monday,12,Sunny
Tuesday,14,Rain
Wednesday,15,Rain
Thursday,14,Cloudy
Friday,21,Sunny
Saturday,22,Sunny
Sunday,24,Sunny

main.py

###Type1:pandas

import pandas
data = pandas.read_csv("weather_data.csv")
print(data)
print(data["temp"])
==================
###Type 2: Using noraml file open method

with open("weather_data.csv") as wether_report:

    print(wether_report.readlines())
    
=========================
    
    
###Type 3: Using csv 

import csv
with open ("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temparature = []
    print(data)
    for row in data:
        if row[1] != "temp":
            temparature.append(int(row[1]))

    print(temparature)
=============================


