import pandas as pd
data=pd.read_csv("D:/coding/pandasapp/electricity.csv",delimiter=";")
print(data)
# data = pd.read_csv("D:/coding/pandasapp/electricity.csv", on_bad_lines="skip")
# print(data)
# data = pd.read_csv("D:/coding/pandasapp/electricity.csv",skiprows=1)
# print(data)
print(data.duplicated())
print(data[""].duplicated().sum())
print(data.drop_duplicates())

