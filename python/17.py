# 1. Write a program to get Fibonacci series up to 10 number
# a=0
# b=1
# n=int(input("enter number here"))
# if n==1:
#     print(1)
# else:
#  print(a)
#  print(b)
# for i in range(2,n):
#     c=a+b
#     a=b 
#     b=c
#     print(c)



# 2. Write a program to check if a number is prime or not.

# num=int(input("enter number here:"))

# if num<=1:
#     print("it is not a prime number")
    
# else:
#     for i in range(2,num):
#        if num%i==0:
#         print("it is not a prime number")    
#         break
#     else:
#         print("it is a prime number")


# 3. Write a program to find a palindrome of integers.
# num=int(input("enter number here:"))
# temp=num
# rev=0
# while num>0:
#     dig=num%10
#     rev=rev*10+dig
#     num=num//10
# if rev==temp:
#    print("it is palindrome")
# else:
#    print("it is not palindrome")    


# 4. Write a program to create an area calculator
print("****area calculator****")
while True:
    print(""""press 1 for finding area of square
    press 2 for finding area of rectangl
    press 3 for finding area of circle""")
    choice=int(input("enter the choice between 1-3"))
    
    if choice==1:
        while True:
            side=float(input("enter the length of one side"))
            area=side**2
            print("the area of square is",area)
            repeat=input("do you want to try again with area of square?")
            if repeat=="no":
                break
    elif choice==2:
        while True:
            length=float(input("enter the length"))
            breadth=float(input("enter the breadth"))
            area=length*breadth
            print("the area of rectangle is",area)
            repeat=input("do you want to try again with area of rectangle?")
            if repeat=="no":
                break
    elif choice==3:
        while True:
            radius=float(input("enter the radius"))
            area=3.14*radius**2
            print("the area of circle is",area)
            repeat=input("do you want to try again with area of circle?")
            if repeat=="no":
                break
    else:
        print("invalid choice! please enter a number between 1-3")                       

