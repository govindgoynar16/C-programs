import pandas as pd
data=pd.read_csv("D:/coding/pandasapp/electricity.csv",delimiter=";")
# print(data)
# print(data.isnull().sum())
# print(data.dropna())
# print(data.mean())
print(data.fillna(method="bfill"))
