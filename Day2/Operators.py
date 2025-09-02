# Python Arithmetic operators are used to perform basic mathematical operations like addition, subtraction, multiplication and division.
print("Arithmetic Operator")
a = 15 
b = 4 
print("Add ", a+b)
print("Subtract ", a-b)
print("Multiply ", a*b)
print("Division ", a/b)
print("Integer Division ", a//b)
print("Modulus ", a%b)
print("Exponential ", a ** b)

# In Python Comparison of Relational operators compares the values. It either returns True or False according to the condition.
print("Relational Operator")
a = 13 
b = 33 
print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

# Python Logical operators perform Logical AND, Logical OR and Logical NOT operations. It is used to combine conditional statements.
print("Logical Operator")
a = True
b = False
print("Logical And " , a and b)
print("Logical Or " , a or b)
print("Logical Not ", not a)

# Python Bitwise operators act on bits and perform bit-by-bit operations. These are used to operate on binary numbers.
# Bitwise Operators in Python are as follows:
# Bitwise NOT
# Bitwise Shift
# Bitwise AND
# Bitwise XOR
# Bitwise OR

print("BitWise Operator")
a = 10 
b = 4
print(a & b)
print(a | b)
print(~a)
print(a ^ b)
print(a >> 2)
print(a << 2)

# Python Assignment operators are used to assign values to the variables. This operator is used to assign the value of the right side of the expression to the left side operand.
print("Assignment Operators ")
a = 10 
b = a
print(b)
b += a
print(b)
b -= a
print(b)
b *= a
print(b)
b //= a
print(b)
b <<= a
print(b)

# In Python, is and is not are the identity operators both are used to check if two values are located on the same part of the memory. Two variables that are equal do not imply that they are identical. 
# is          True if the operands are identical 
# is not      True if the operands are not identical 
print("Identical Operators ")
a = 10 
b = 10 
c = a
print(a is not b)
print(a is c)

# In Python, in and not in are the membership operators that are used to test whether a value or variable is in a sequence.
# in            True if value is found in the sequence
# not in        True if value is not found in the sequence
print("Membership Operators ")
x = 24 
y = 20 
list = [10,20,30,40,50]

if(x not in list):
    print("x is not present in list")
else:
    print("x is present in list")

if(y in list):
    print("y is present in list")
else:
    print("y is not present in list")
    
# in Python, Ternary operators also known as conditional expressions are operators that evaluate something based on a condition being true or false. It was added to Python in version 2.5. 
# It simply allows testing a condition in a single line replacing the multiline if-else making the code compact.
# Syntax :  [on_true] if [expression] else [on_false] 
print("Ternary Operator")
a , b = 10 , 20 
min = a if a < b else b
print(min)

# Precedence and Associativity of Operators

# In Python, Operator precedence and associativity determine the priorities of the operator.
# Operator Precedence
# This is used in an expression with more than one operator with different precedence to determine which operation to perform first.

print("Operator Precedence")
expr = 10 + 20 * 30
print(expr)
name = "Alex"
age = 0
if name == "Alex" or name == "John" and age >= 21:
    print("Hello welcome")
else:
    print("Bye")
    
# If an expression contains two or more operators with the same precedence then Operator Associativity is used to determine. It can either be Left to Right or from Right to Left.
print("Operator Associativity")
print(100 / 10 * 10)
print(5 - 2 + 3)
print(5 - (2 + 3))
print(2 ** 3 ** 2)