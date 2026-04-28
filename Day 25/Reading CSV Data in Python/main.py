import pandas


# import csv

PATH = "/Users/liuyuchen/Downloads/General Coding/Dr.Angela Yu's 100Day python challenge/Day 25/Reading CSV Data in Python/Data/weather_data.csv"

# with open(PATH,mode="r") as file:
#     data = csv.reader(file)
#     temperatures = []

#     for row in data:
#         try:
#             temperatures.append(int(row[1]))
#         except ValueError:
#             temperatures.append(row[1])

#     print(temperatures)

myData = (pandas.read_csv(PATH))

for i in myData:
    print(i)