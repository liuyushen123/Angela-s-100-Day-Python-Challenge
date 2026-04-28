import pandas as pd


PATH = "/Users/liuyuchen/Downloads/General Coding/Udemy Course/AngelaYu_100DaysPython/Day 25/DataFrames & Series/weather_data.csv"
data = pd.read_csv(PATH)

averageTemperture = sum(data["temp"].to_list()) // len(data["temp"].to_list())
print(data)
print(averageTemperture)
print(data["temp"].median())
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])


data_dict = {
    "students": ["Yuchen", "Will", "Josh", "Jackson", "James"],
    "score": [56, 92, 82, 87, 96],
}

student_data = pd.DataFrame(data_dict)
student_data.to_csv("new_data.csv")
