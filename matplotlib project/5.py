# import matplotlib.pyplot as plt
# import numpy as np 
# x=np.random.randint(1,10,50)
# y=np.random.randint(10,100,50)
# color=np.random.randint(10,100,50)
# plt.scatter(x,y,marker="*",c= color,cmap="hot")
# plt.colorbar()
# plt.show()

import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 

data=pd.read_excel("D:/coding/pandasapp/EE_DATA.xlsx")
df=pd.DataFrame(data)
print(df)
plt.scatter(df["Location"],df=["Date Hired"])
plt.scatter(df["Sex"],df["Salary"])
plt.show()