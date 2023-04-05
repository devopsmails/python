link: http://pandas.pydata.org/docs/reference/frame.html

pandas dataframes- Serialization / IO / conversion: helps to convert from one data type to another

Example:

1.main.py


import pandas
data = pandas.read_csv("weather_data.csv")
data_table = data.to_excel
data_diction = data.to_dict()
print(data_diction)
data_list = data["temp"].to_list()
print(data_list)

===================

2. weather_data.csv

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
