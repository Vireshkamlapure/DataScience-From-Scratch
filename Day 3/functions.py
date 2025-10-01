# Python Functions are a block of statements that does a specific task. The idea is to put some commonly or repeatedly done task together and make a function so that instead of writing the same code again and again for different inputs, we can do the function calls to reuse code contained in it over and over again.
def function_hello():
    print("Hello world")
    return 0

function_hello()

# Explanation:
# def: Starts the function definition.
# function_name: Name of the function.
# parameters: Inputs passed to the function (inside ()), optional.
# Indented code: The function body that runs when called.

# Function Arguments : Arguments are the values passed inside the parenthesis of the function. A function can have any number of arguments separated by a comma.

def evenOdd(x):
    if x%2 == 0:
        return "Even"
    else:
        return "Odd"
print(evenOdd(3))

# Types of Function Arguments
# Default Arguments : A default argument is a parameter that assumes a default value if a value is not provided in the function call for that argument.

def myFunc(x,y=50):
    print("x : ",x," y : ",y)

myFunc(4)
myFunc(4,44)

# 2. Keyword Arguments : In keyword arguments, values are passed by explicitly specifying the parameter names, so the order doesn’t matter.
def student(fname , lname):
    print(fname , lname)

student(fname="geeks",lname="practice")
student(lname="practice",fname="geeks")

# 3. Positional Arguments : In positional arguments, values are assigned to parameters based on their order in the function call.
def nameAge(name , age):
    print("Hii i am ",name)
    print("I am ",age," years old")

nameAge("viraj",21)
nameAge(21,"viraj")

# 4. Arbitrary Arguments

# In Python Arbitrary Keyword Arguments, *args and **kwargs can pass a variable number of arguments to a function using special symbols. There are two special symbols:

# *args in Python (Non-Keyword Arguments)
# **kwargs in Python (Keyword Arguments)

def myFun(*args , **kwargs):
    print("Non-keyword arguments : ")
    for arg in args:
        print(arg)
    
    print("keyword arguments : ")   
    for kwarg in kwargs:
        print(kwarg)
    
myFun("Hey" , "welcome" , first="Geeks" , mid="for" , last="Geeks")

# Function within Functions
# A function defined inside another function is called an inner function (or nested function). It can access variables from the enclosing function’s scope and is often used to keep logic protected and organized.

def f1():
    s = "I love my india"
    def f2():
        print(s)
    
    f2()

f1()

# Anonymous Functions : In Python, an anonymous function means that a function is without a name. As we already know the def keyword is used to define the normal functions and the lambda keyword is used to create anonymous functions.

def cube(x): return x*x*x
cube_l = lambda x : x*x*x 

print(cube(7))
print(cube_l(7))

# Pass by Reference and Pass by Value

# In Python, variables are references to objects. When we pass them to a function, the behavior depends on whether the object is mutable (like lists, dictionaries) or immutable (like integers, strings, tuples).

# Mutable objects: Changes inside the function affect the original object.
# Immutable objects: The original value remains unchanged.

def myFun2(x):
    x[0] = 20
    
lst = [10,20,30,40]
myFun2(lst)
print(lst)

def myFun3(x):
    x = 20

a = 10
myFun3(a)
print(a)

# Note: Technically, Python uses "pass-by-object-reference". Mutable objects behave like pass by reference, while immutable objects behave like pass by value

# Recursive Functions :  A recursive function is a function that calls itself to solve a problem. It is commonly used in mathematical and divide-and-conquer problems. Always include a base case to avoid infinite recursion.

def factorial(n):
    if n == 0:
        return 1
    else : 
        return n * factorial(n-1)
    
print(factorial(4))