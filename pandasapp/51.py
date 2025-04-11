import pandas as pd
data=pd.read_excel(r"D:/coding/pandasapp/EE_DATA.xlsx")
# print(data.head(15))
# print(data["Salary"])
# print(data.columns)
print(data.loc[:, "Salary"])
data["bonus"]=(data["Salary"]/100)*20
print(data.head(10))

