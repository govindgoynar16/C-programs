import pandas as pd 
import matplotlib.pyplot as plt
data=pd.read_excel("D:/coding/matplotlib project/BlinkIT Grocery Data Excel.xlsx")
df=pd.DataFrame(data)
grouped_by=df.groupby("Item Weight")["Sales"].sum()
print(grouped_by)
plt.plot(grouped_by.index,grouped_by.values)

# plt.plot(df["Outlet Type"],df["Rating"])
print(df)
plt.show()
