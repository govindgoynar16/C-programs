import pandas as pd
# dict={"Keys":["k1","k2","k1","k1"],
#     "Names":["john","Ben","david","peter"],
#    "Houses":["red","blue","green","red"],
#    "Grades":["3rd","8th","9th","8th"]}
# df=pd.DataFrame(dict)   
# print(df)
# print(df.pivot(index="keys", columns="Names", values=["Houses","Grades"]))

dict={"Names":["john","Ben","david","peter"],
   "Houses":["red","blue","green","red"],
   "Grades":["3rd","8th","9th","8th"]}
df=pd.DataFrame(dict)
print(df)
print(pd.melt(df,id_vars=["Names"],value_vars=["Houses","Grades"],var_name="Houses&Grades",value_name="values"))