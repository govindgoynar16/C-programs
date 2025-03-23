# 1. Write a function to find maximum of three numbers in Python.
# def maximum_num(val1,val2,val3):
#     if val1>val2 and val1>val3:
#         print(val1,"is the greatest number")
#     elif val2>val3 and val2>val1:
#         print(val2,"is the greatest number")
#     else:
#         print(val3,"is the greatest number") 
# maximum_num(12,5,8)     
# 2. Write a Python function to create and print a list where the values are square of numbers between 1 and 30.
# def create_list():
#     l=[]
#     for i in range(1,31):
#         l.append(i**2)
#     return l
# print(create_list())        
# 3. Write a Python function that takes a number as a parameter and check if the number is prime or not.
# def check_prime(num):
#     if num<=1:
#         print("it is not a prime no.")
#     if num==2:
#         print("it is prime no.") 
#     if num>2:      
#         for i in range(2,num):
#             if num%i==0:
#                 print("it is not a prime no.") 
#                 break
#         else:
#             print("it is prime no.")  
# check_prime(3)                      
# 4. Write a Python function to sum all the numbers in a list.
# def add(num):
#     total=0
#     for i in num:
#         total=total+i
#     return (total)
# print("the sum of all the items in list",add([12,4,5,6,7,8])) 

#solution through using recurssion
# def add(numbers):
#     if len(numbers)==1:
#         return(numbers[0])
#     else:
#        return((numbers[0])+add(numbers[1:]))
# print(add([12,4,5,6,7,8]))    

# 5. Write a Python program to solve the Fibonacci Sequenence using Recursion.
# def fib(num):
#    if num==1:
#     return(0)
#    elif num==2:
#     return(1)
#    else:
#     return(fib(num-1)+fib(num-2))
# print(fib(21))    
