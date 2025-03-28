import numpy as np
# a=np.array([20,40,60,90])
# print(np.sum(a))
# print(np.min(a))
# print(np.max(a))
# print(np.size(a))
# print(np.mean(a))
# print(np.cumsum(a))
# print(np.cumprod(a))

a=[100,150,30,199,200,140]
b=[10,50,40,100,30,45]
price=np.array(a)
quantity=np.array(b)
print(price,"\n",quantity)
print()
c=np.cumprod([price,quantity],axis=0)
print(c[1].sum())

