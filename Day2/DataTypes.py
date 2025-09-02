# Numeric - int, float, complex
# Python numbers represent data that has a numeric value. A numeric value can be an integer, a floating number or even a complex number. These values are defined as int, float and complex classes.
a = 5
print(type(a))
a = 5.5 
print(type(a))
a = 2 + 3j
print(type(a))
# Sequence Type - string, list, tuple
# The sequence Data Type is ordered collection of similar or different Python data types. Sequences allow storing of multiple values in an organized and efficient fashion. 
s = "Welcome to python tutorial"
print(s)
print(type(s))
print(s[1])
print(s[2])
print(s[-1])
#List
#empty list 
a = [] 
print(a)
#list with int values 
a = [1,2,3]
print(a)
#list with mixed values 
a = ["Hello" , "World" , 615 , 5.5] 
print(a)
print(a[1])
print(a[-1])
print(a[-2])
#Tuple 
tup1 = ()
tup2 = ('Geeks','For',5,9.9)
print(tup2)
print(tup2[0])
print(tup2[-1])
print(tup2[-3])
# Mapping Type - dict
d1 = {} 
d = {1:"Geeks" , 
     2 : "For" , 
     3 : "Geeks"}
print(d)

d1 = dict({1:"Hello" , 2: "World" , 3:"India"})
print(d1)
d2 = dict({'name':"John" , 'age':32})
print(d2['name'])
print(d2.get('age'))
# Boolean - bool
print(type(True))
print(type(False))
# print(type(true)) --> Python is case-sensitive. 
# Set Type - set, frozenset
#set 
s1 = set()
s1 = set("GeeksforGeeks")
print("Set with the use of String: ", s1)
s2 = set(["Geeks", "For", "Geeks"])
print("Set with the use of List: ", s2)
s3 = {"Hello","Workds" , 34}
print(type(s3))
print(s3)
for i in s1 :
    print(i,end=" ")
print("Geeks" in s2)
# Binary Types - bytes, bytearray, memoryview