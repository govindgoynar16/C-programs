#endswith returns true if the string end with specified value
a="harry potter"
print(a.endswith("t",6,9))

#startswith() returns true if the string starts with the specified value
print(a.startswith("h"))

#swapcase() swap case,lower case becomes upper case and vice versa
print(a.swapcase())

#strip() returns a trimmed version of the string
A="      harry Potter     "
print(A.strip())

#split() split  the string at the specified seperator and returns a list
B="%OOfd%Bbrd%omw%tb"
print(B.split("%"))

#ljust() returns a left justified version of the string
x=a.ljust(20,"*")
print(x,"is my favourite movie")

#rjust() returns a right specified version of the string
x=a.rjust(20,"*")
print(x,"is my favourite movie")

#replace() returns a string where a specifeid value is replaced with a specified value
print(a.replace("potter","doctor"))

#rindex() searches the string for a specified value and returns the last position of where it was found 
u="harry potter is a very decent movie and got a gallantry award"
print(u.rindex("movie"))
#r.find() searches the string for a specified value and returns the last position of where it was found 
print(u.rfind("a",14,50))
