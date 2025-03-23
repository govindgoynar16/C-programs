# def hello():
#     print("hello world")
# hello()    


# def add(x,y):
#    print(x+y)
# add(4,5)    

# def rect(length,width,height):
#     print("the volume of the cuboid is",length*width*height)
# rect(12,3,12)    
# # arbitarory arguments 
# def hello(*name):
#     print("hello my name is",name[1])
# hello("govind","shubh","diwakar")    


# def hello():
#     return("hello world")
# print(hello())    

# def add(a,b):
#     return("the addition of two number is",a+b)
# print(add(12,4))   


# recurrsion

# def hello():
#     print("hello")
#     return hello()
# print(hello())

def fact(n):
    if n==1:
        return 1
    else:
        return (n*fact(n-1))
print(fact(6))   

