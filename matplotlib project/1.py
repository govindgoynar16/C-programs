import matplotlib.pyplot as plt

y=[98,67,88,95,88]
x=["part1","part2","part3","part4","part5"]
color=["red","green","pink","yellow","orange"]
plt.bar(x,y,color= color)
plt.xlabel("part of harry potter",fontsize =17)
plt.ylabel("popularity",fontsize =17)
plt.title("popularity of different parts of harry potter",fontsize =21)
plt.show()

