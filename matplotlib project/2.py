import pandas as pd 
import matplotlib.pyplot as plt
data=pd.read_excel("D:/coding/matplotlib project/BlinkIT Grocery Data Excel.xlsx")
df=pd.DataFrame(data)
print(df.head(10))
grouped_by=df.groupby("Outlet Establishment Year")["Sales"].sum()
print(grouped_by)
plt.bar(df["Outlet Establishment Year"],df["Sales"])
plt.xlabel("Outlet Establishment Year")
plt.ylabel("Sales")
plt.show()