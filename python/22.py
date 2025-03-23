a=["ironman","hulk","thor","captain america","hulk"]
#to find the length of a list
print(len(a))
#to count on occurence of a particular element 
print(a.count("hulk"))
# to add to the list
a.append("spiderman")
print(a)
#to add to a specific location
a.insert(2,"vision")
print(a)
#to remove from a list
a.remove("spiderman")
print(a)
#to remove from a certain location
print(a.pop(1))
print(a)