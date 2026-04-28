import pandas as pd

data = {
    "name": ["Kofi", "Ama", "Kwame"],
    "age": [20, 22, 21],
    "grade": [85, 92, 78] } 

df = pd.DataFrame(data)
print(df)
print(df["name"])
print(df.iloc[0])
print(df[df["grade"] > 80])
print(df.describe())