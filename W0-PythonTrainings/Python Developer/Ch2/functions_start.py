#
# Example file for working with functions
#

# define a basic function
def func1():
    print("I am a function")

# function that takes arguments
def functionArgs(arg1, arg2):
    return arg1*arg2

# function that returns a value
def funLoop(arg1,count=1):
    c=0
    b=1
    a=0
    for i in range(count):
       c=a+b
       a=b
       b=c
       print(c**b) 
    return c

# function with default value for an argument
def square(x=2):
    return x*x

#function with variable number of arguments

# func1()
#print(func1())
#print(func1)
# print(square())
# print(square(functionArgs(2,2)))
funLoop(1,20)