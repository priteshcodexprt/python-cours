#function code
from itertools import product
from re import S


def percent(marks): 
    p=((marks[0]+marks[1]+marks[2]+marks[3])/400)*100
    return p

marks=[45,88,5,55]
percentage1 = percent(marks)

marks2=[77,88,66,55]
percentage2=percent(marks2)
print(percentage1,percentage2)


# quick_quiz code
def greet (name):
    print("goodmoornig,"+name)

def mySum(num1,num2):
    return num1,num2

greet("pritesh")
s=mySum(8,32)
print(S)

# default_argument code
def greet (name="strange"):
    print("goodmoornig,"+name)


greet("pritesh")
greet()

# factorial code

def factorial_iter(n):
    product=1
    for i in range(n):
        product=product*(i+1)
    return product

def factorial_recursive(n):
    if n==0 or n==1:
        return 1
    return n * factorial_recursive(n-1)

print(factorial_recursive(10))








