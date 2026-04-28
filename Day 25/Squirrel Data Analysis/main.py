import pandas as pd

PATH = "SquirrelData.csv"

data = pd.read_csv(PATH)

Black_squirrel = 0
Gray_squirrel = 0
Cinnamon_squirrel = 0

for i in data["Primary Fur Color"]:
    if i == "Cinnamon":
        Cinnamon_squirrel += 1
    elif i == "Gray":
        Gray_squirrel += 1
    elif i == "Black":
        Black_squirrel += 1

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [Gray_squirrel, Cinnamon_squirrel, Black_squirrel],
}

df = pd.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
