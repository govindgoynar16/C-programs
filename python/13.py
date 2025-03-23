a="Harry Potter and the Goblet of Fire"
print(a)
# to find the length
print(len(a))
# to count specific letter in whole sentence 
print(a.count("t"))
#to find how many upper case and lower case
print(a.upper())
print(a.lower())
# to indexing the letter
print(a.index("G"))
# to capitalize the first letter of first word
print(a.capitalize())
# convert upper case in to lower case
print(a.casefold())
# to find the index number of character
print(a.find("t",15,34))
#  to write variable inside a string
name="john"
age=20
b= "my name is {} \n my age is {}"
print(b.format(name,age))

# it fills the given characters and centralizes a string
print(name.center(20,"*"))