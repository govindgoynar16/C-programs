import pandas as pd

# Load Excel file (use full path if not in the same directory)
data = pd.read_excel("D:/coding/pandasapp/class.xlsx")

# Display the first 5 rows
print(data.head(20))
# print(data.tail(20))
# print(data.info())
# print(data.describe())
# print(data.isnull())
# print(data.isnull().sum())
