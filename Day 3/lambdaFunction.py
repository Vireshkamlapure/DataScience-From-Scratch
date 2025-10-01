# Lambda Functions are anonymous functions means that the function is without a name. As we already know def keyword is used to define a normal function in Python. Similarly, lambda keyword is used to define an anonymous function in Python. 
s1 = "geeksforgeeks"
s2 = lambda func : func.upper()
print(s2(s1))

# Syntax :  lambda arguments : expression
# lambda: The keyword to define the function.
# arguments: A comma-separated list of input parameters (like in a regular function).
# expression: A single expression that is evaluated and returned.

# Use Cases of Lambda Functions
# 1. Using with Condition Checking
n = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"
print(n(5))
print(n(-5))
print(n(0))

check = lambda x: "Even" if x%2==0 else "Odd"
print(check(99))

# 2. Using with List Comprehension
li = [lambda arg=x : arg*10 for x in range(1,5)]
for i in li:
    print(i())

# 3. Using for Returning Multiple Results
calc = lambda x,y : (x+y , x*y)
print(calc(3,4))

sqcu = lambda x : (x*x , x*x*x)
print(sqcu(3))

# 4. Using with filter() : The filter() function in Python takes in a function and a list as arguments. This offers an elegant way to filter out all the elements of a sequence "sequence", for which the function returns True.
n = [1,2,3,4,5,6,7,8,9,0] 
even = filter(lambda x : x%2==0 , n)
print(list(even))

# 5. Using with map() : The map() function in Python takes in a function and a list as an argument. The function is called with a lambda function and a new list is returned which contains all the lambda-modified items returned by that function for each item.

a = (1,2,3,4)
sqmapped = map(lambda x: x*x , a)
print(list(sqmapped))

# 6. Using with reduce() : The reduce() function in Python takes in a function and a list as an argument. The function is called with a lambda function and an iterable and a new reduced result is returned. This performs a repetitive operation over the pairs of the iterable. The reduce() function belongs to the functools module. 

from functools import reduce
a = [1,2,3,4] 
b = reduce(lambda x,y : x*y , a)
print(b)

# Difference Between lambda and def Keyword

# In Python, both lambda and def can be used to define functions, but they serve slightly different purposes. While def is used for creating standard reusable functions, lambda is mainly used for short, anonymous functions that are needed only temporarily.


# Feature	   |    lambda Function	                   | Regular Function (def)
# Definition.  |    Single expression with lambda.	   | Multiple lines of code.
# Name	       |    Anonymous (or named if assigned).  | Must have a name.
# Statements.  |    Single expression only.	           | Can include multiple statements.
# Documentation|    Cannot have a docstring.	       | Can include docstrings.
# Reusability. |    Best for short,temporary functions.| Better for reusable & complex logic.
