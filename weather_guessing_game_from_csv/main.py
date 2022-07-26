# Read data from csv file.
"""
with open("weather_data.csv") as data_file:
    data = data_file.readlines()
    print(data)
However, the output shows each line separated by commas, which makes it hard to work with.
['day,temp,condition\n', 'Monday,12,Sunny\n', 'Tuesday,14,Rain\n', 'Wednesday,15,Rain\n', 'Thursday,14,Cloudy\n', 'Friday,21,Sunny\n', 'Saturday,22,Sunny\n', 'Sunday,24,Sunny']


import csv

# Therefore, we can use the pre-built csv.reader to perform this task efficiently.
with open("weather_data.csv") as data_file:
    # csv reader will read line by line and assign them inside an array of lists.
    data = csv.reader(data_file)
    temperature = []

    for row in data:
        if row[1] != "temp":
            temperature.append(int(row[1]))
    print(temperature)


import pandas
data = pandas.read_csv("weather_data.csv")
print(type(data["temp"]))

OUtput:
         day  temp condition
0     Monday    12     Sunny
1    Tuesday    14      Rain
2  Wednesday    15      Rain
3   Thursday    14    Cloudy
4     Friday    21     Sunny
5   Saturday    22     Sunny
6     Sunday    24     Sunny

"""

import pandas
data = pandas.read_csv("weather_data.csv")
data_dict = data.to_dict()
print(type(data["temp"].max()))