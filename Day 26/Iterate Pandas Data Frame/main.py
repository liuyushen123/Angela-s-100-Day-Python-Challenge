import pandas as pd

stduent_dict = {"student": ["Will", "Josh", "Yuchen"], "score": [55, 86, 90]}

pdFrame = pd.DataFrame(stduent_dict)


for index, row in pdFrame.iterrows():
    print(index)  ### The first value will just be row index number
    print(row.score)  ### The second one will be the entire row!
    print(row.student)
