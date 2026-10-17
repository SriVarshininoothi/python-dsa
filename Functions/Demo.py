
def greet():
    print("Hello World")

greet()


def add(a,b):

    return a+b
s = add(1,2)
print(s)


def intro(name,age):
    print(name,age)

intro("Ravi",22)


def student(name,age,city):

    print(name,age,city)

student(name="Leela",age=23,city="Hyd")


 

def greet(name,message='Welcome'):
    print(message,name)

greet("Ravi")
greet("Ravi","good Morning")


def total(*args):

    print(args)
    return sum(args)
print(total(10,20))
print(total(5,10,15,20))


def intro(**kwargs):

    print(kwargs["name"])
    print(kwargs["age"])

intro(name="Srivarshini",age=23)

#mutiple return values

def calculate(a,b):

    total = a+b
    product = a*b

    return total,product

x,y = calculate(5,3)
print(x,y)

def min_max(numbers):

    return min(numbers),max(numbers)

small, large = min_max([4,9,2,7])
print(small,large)


#local scope

def demo():
    x=10
    return x
print(demo())

#Global

x = 10
def demo1():
    print(x)
demo1()


#function composition

def double(x):
    return x*2
def add(x):
    return x+10

result = double(15)
result1 = add(result)
print(result)
print(result1)


#Recursion

def countdown(n):

    if n == 0:
        return 
    
    print(n)

    countdown(n-1)
    
countdown(3)


def sum_number(n):

    if n == 0:
        return 0

    return n + sum_number(n-1)

print(sum_number(5))


def fact_number(n):

    if n==0:

        return 1

    return n * fact_number(n-1)

print(fact_number(5)) 




    

