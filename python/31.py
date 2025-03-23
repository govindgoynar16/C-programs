# a={"ironman","hulk","thor","captain america"}
# print(a)
# print(type(a))
# for x in a:
#     print(x)


#add
# a.add("spiderman")
# print(a)
#pop
# a.pop()
# print(a)
#remove
# a.remove("hulk")
# print(a)
#discard
# a.discard("thor")
# print(a)
#copy
# b=a.copy()
# print(b)
a={"ironman","hulk","thor","captain america"}
b={"superman","wonderwoman","batman"}
c={"hulk","thor","spiderman"} 
#isdisjoint
# print(a.isdisjoint(b))
#issubset
# print(c.issubset(a))
#issuperset
# print(a.issuperset(c))
#update
# a.update(c)
# print(a)
#clear
# a.clear()
# print(a)
#union
# print(a.union(b))
#difference
# print(a.difference(c))
#difference update
# a.difference_update(c)
# print(a)
#intersection
# print(a.intersection(c))
#intersection update
# a.intersection_update(c)
# print(a)
#symmetric difference
# x=a.symmetric_difference(b)
# print(x)
#symmetric difference update
a.symmetric_difference_update(c)
print(a)

