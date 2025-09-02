age = 20 
# if Statement 
if age >= 18:
    print("You are eligible for voting.")
    
# Short Hand if
if age >= 18 : print("Eligible to vote.")

# If else Conditional Statement
age = 13
if age <= 12:
    print("Travel for free")
else:
    print("Pay to travel")

# Short hand if else 
marks = 45 
res = "Pass" if marks >= 40 else "Fail"
print(res)

# elif Statement
age = 25

if age <= 12:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 35:
    print("Young adult")
else :
    print("Adult")

# Nested if..else Conditional Statement
age = 70 
is_member = True 
if age >= 60:
    if is_member:
        print("30% senior discount")
    else:
        print("20% seior discount")
else:
    print("Not eligible for senior discount")
    
# Match-Case Statement

# match-case statement is Python's version of a switch-case found in other languages. It allows us to match a variable's value against a set of patterns.
number = 2
match number:
    case 1:
        print("One")
    case 2 | 3: 
        print("Two or three")
    case _ :
        print("Other number")

x = 4
print(id(x))
# print(id(int)(x+"GFG"))

s = "gfg"
print(("g" or "") in s)

print(oct(23))