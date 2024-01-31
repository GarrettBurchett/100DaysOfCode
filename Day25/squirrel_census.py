import pandas as pd

squirrel_data = pd.read_csv("Day25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#print(squirrel_data.columns)
fur_color_counts = squirrel_data["Primary Fur Color"].value_counts()
fur_color_counts.to_csv("Day25/squirrel_count.csv")