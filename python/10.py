# 1. Write a program to find a sum of all the even numbers up to 50.
# sum=0
# for i in range(1,51):
    
#     if i%2==0:
#        sum+=i
   
# print( "the sum of all the even numbers up to 50 is",sum)


# 2. Write a program to write first 20 numbers and their squared numbers.

# for i in range(1,21):
#     print(i,i**2)


# 3. Write a program to find sum of first 10 odd numbers using while loop.
# sum=0
# n=0
# while n<=20:
#     if n%2!=0:
#         sum+=n
#     n+=1
# print("sum of first 10 odd number is",sum)        

# 4. Write a program to check if a number is divisible by 8 and 12 100 numbers to
# for i in range(1,101):
#     if i%8==0 and i%12==0:
#      print(i)

# 5. Write a program to create a billing system at supermarket
# while True:
#   name=input("put customer name")
#   total=0
#   while True:
#     print("enter the amount and quantity")
#     amount=float(input("enter amount"))
#     quantity=float(input('enter quantity'))
#     total+=amount*quantity
#     repeat=input("do you want to add more items?(yes/no):")
#     if repeat=="no" or repeat=="No":
#         break

#   print("-" *40)
#   print("customer name",name)
#   print("amount to be paid:",total)
#   print("-" *40)
#   print("**happy shoppping**")

#   repeat1=input("do you want to go to next customer?(yes/no):")
#   if repeat1=="no" or repeat=="No":
#       break