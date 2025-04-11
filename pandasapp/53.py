import pandas as pd
data=pd.read_excel(r"D:/coding/pandasapp/EE_DATA.xlsx")
print(data.head(15))
gp=data.groupby("Location").agg({"Sex":"count"})
print(gp)
gp1=data.groupby(["Location","Sex"]).agg({"Salary":"mean"})
print(gp1)