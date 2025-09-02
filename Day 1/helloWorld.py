# name = input("Enter Your Name : ")
#Typecat input into int
# age = int(input("Enter Your Roll No : "))
# print("Hello ",name," Welcome!!")

#Multiple Input 
# x , y = input("Enter two values : ").split()
# print("Value of x : ",x)
# print("Value of y : ",y)
x = 5

#Find Data type : 
print(type(x))

#Output Formating : 
# 1.Using format() 
amount = 33.55
print("Amount : ${:.2f}".format(amount))

# 2.Using Sep (Seperator) and end parameter 
print("Python" ,end="@")
print("GFG")

print("22","July","2025", sep="-")

# 3.Using f-String 
name = "Viraj"
age = 21 
print(f"The Student named {name} is {age} year's old")

# 4. Using % symbol 
a = 22 
b = "rohit"
c = 44.5 

print("The b %s " %b)
print("The a %i " %a)
print("The c %f " %c)

# %d = int 
# %f = float 
# %s = string 
# %x = hexadecimal 
# %o = octal
