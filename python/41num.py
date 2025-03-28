# method to concatenate
import numpy as np
arr1=np.array([[20,30],[40,70]])
arr2=np.array([[5,5],[3,5]])
# print(np.concatenate([arr1,arr2]))
# print(np.concatenate([arr1,arr2],axis=1))
# print(np.hstack([arr1,arr2]))#horizontal concatenate
# print(np.vstack([arr1,arr2]))#vertical concatenate
a=np.array([[20,30,40],[50,60,90]])
b=np.array_split(a,3)
print(b)