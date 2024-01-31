# with open("./Day25/weather_data.csv") as w:
#     contents = w.readlines()
# print(contents)

# import csv

# with open("./Day25/weather_data.csv") as w:
#     data = csv.reader(w)
#     temperatures = [int(row[1]) for row in data if row[1] != 'temp']
#     print(temperatures)

import pandas as pd

weather_data = pd.read_csv("./Day25/weather_data.csv", header=0, dtype={'temp': pd.Int8Dtype()})
# avg_temp = weather_data["temp"].mean()
def convert_C_to_F(temperature):
    return temperature * 1.8 + 32

print(convert_C_to_F(weather_data.temp[0]))