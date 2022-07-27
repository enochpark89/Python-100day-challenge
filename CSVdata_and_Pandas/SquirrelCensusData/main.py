"""
Objective:
Read downloaded csv and count different fur colors.
Then, create a new data frame that stores that information.
"""

import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# Get a total count of squirrels with different fur colors.
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

# Add counts into the dictionary.
data_dict =  {
    "Fur Color": ["Grey", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

# create a new data frame with the result.
df = pandas.DataFrame(data_dict)

# export to file
df.to_csv("squirrel_count.csv")