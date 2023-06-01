link: http://pandas.pydata.org/docs/reference/frame.html

pandas dataframes- Serialization / IO / conversion: helps to convert from one data type to another

Example:

1.main.py
==========

import pandas
data = pandas.read_csv("weather_data.csv")
data_table = data.to_excel
data_diction = data.to_dict()
print(data_diction)

#to list
data_list = data["temp"].to_list()
print(data_list)

#average
average = round(data["temp"].mean(),2)
print(average)

#max
max = data["temp"].max()
print(f"maximum temparature is {max}")

#get data column
#type1:
print(data["condition"])

#type2:
print(data.condition)

#get data in a row

print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
monday_temp_f = monday_temp * 9/5 + 32
print(monday_temp_f)

#How to create a data frame from scratch

data_dict = {
    "students" : ["Suresh", "ramesh", "Rahul"],
    "marks" :  [76, 70, 80]
}
data1 = pandas.DataFrame(data_dict)
print(data1)
#creates a new csv file in the current path
data1.to_csv("new_data.csv")

===================

2. weather_data.csv
==================

day,temp,condition
Monday,12,Sunny
Tuesday,14,Rain
Wednesday,15,Rain
Thursday,14,Cloudy
Friday,21,Sunny
Saturday,22,Sunny
Sunday,24,Sunny

=================

Results
===============
      
{'day': {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}, 'temp': {0: 12, 1: 14, 2: 15, 3: 14, 4: 21, 5: 22, 6: 24}, 'condition': {0: 'Sunny', 1: 'Rain', 2: 'Rain', 3: 'Cloudy', 4: 'Sunny', 5: 'Sunny', 6: 'Sunny'}}
[12, 14, 15, 14, 21, 22, 24]
17.43
maximum temparature is 24
0     Sunny
1      Rain
2      Rain
3    Cloudy
4     Sunny
5     Sunny
6     Sunny
Name: condition, dtype: object
0     Sunny
1      Rain
2      Rain
3    Cloudy
4     Sunny
5     Sunny
6     Sunny
Name: condition, dtype: object
      day  temp condition
0  Monday    12     Sunny
      day  temp condition
6  Sunday    24     Sunny
53.6
  students  marks
0   Suresh     76
1   ramesh     70
2    Rahul     80




