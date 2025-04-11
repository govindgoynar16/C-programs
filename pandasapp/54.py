import pandas as pd
# data1={"Emp Id":["E01","E02","E03","E04","E05","E06",],
# "Names":["Ram","shyam","ghanshyam","Rambati","Ramlakhan","Ramnavami"],
# "Age":[34,56,23,44,52,65]}

# data2={"Emp Id":["E01","E02","E03","E04","E05","E06",],
# "Salary":[23000,30000,40000,50000,25000,45000]}
# df1=pd.DataFrame(data1)
# df2=pd.DataFrame(data2)
# print(df1)
# print()
# print(df2)
# print(pd.merge(df1,df2,on="Emp Id"))
# print(pd.merge(df1,df2,on="Emp Id",how="inner"))
# print(pd.merge(df1,df2,on="Emp Id",how="left"))

data1={"Emp Id":["E01","E02","E03","E04","E05","E06",],
"Names":["Ram","shyam","ghanshyam","Rambati","Ramlakhan","Ramnavami"],
"Age":[34,56,23,44,52,65]}

data2={"Emp Id":["E07","E08","E09","E10","E11","E12",],
"Names":["aam","daam","chotu","gannu","paro","harshu"],
"Age":[34,56,23,44,52,65]}
df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2)
print(pd.concat([df1,df2]))