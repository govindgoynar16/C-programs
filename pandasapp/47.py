import pandas as pd

# Load Excel file (use full path if not in the same directory)
data = pd.read_excel(r"D:/coding/pandasapp/class.xlsx")

# Display the first 5 rows
print(data.head(20))