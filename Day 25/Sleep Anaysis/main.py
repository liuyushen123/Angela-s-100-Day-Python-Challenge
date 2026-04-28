import pandas as pd
import math

PATH = "Sleep_health_and_lifestyle_dataset.csv"
data = pd.read_csv(PATH)

allOccupations = data["Occupation"].unique()
allOccupationscount = data["Occupation"].value_counts()

print(allOccupationscount)
sleepDurationAvg = {}
stressLevelAvg = {}

for i in allOccupations:
    sleepDuration = data[data.Occupation == i]["Sleep Duration"].mean()
    print()
    print(f"{i} has average sleep duration of {sleepDuration:.2f}")
    print()
    sleepDurationAvg[i] = math.floor(sleepDuration)


for i in allOccupations:
    stressLevel = data[data.Occupation == i]["Stress Level"].mean()
    print()
    print(f"{i} has average stress level of {stressLevel:.2f}")
    print()
    stressLevelAvg[i] = math.floor(stressLevel)


sorted_sleep = dict(sorted(sleepDurationAvg.items(), key=lambda x: x[1]))
sorted_stress = dict(sorted(stressLevelAvg.items(), key=lambda x: x[-1], reverse=True))

print(sorted_sleep)
print(sorted_stress)
