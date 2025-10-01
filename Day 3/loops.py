#for loop
n = 4
for i in range(0,n):
    print(i)

l1 = ['Hii', 29 , 'geeks' , 'tutorial' , 4.33, False] 
for i in l1:
    print(i)
    
t1 = ('heoll' , 69 , True)
for i in t1:
    print(i)

d1 = {1:"One" , 3 : "Three" , 5:"Four"} 
for i in d1:
    print(i , d1[i])

s1 = (12,22,32,43,54)
for i in s1:
    print(i)
    
l2 = ['geeks' , 'for' , 'geeks']
for i in range(len(l2)):
    print(l2[i])
else:
    print ("Inside else block")
    
# While Loop

# In Python, a while loop is used to execute a block of statements repeatedly until a given condition is satisfied. When the condition becomes false, the line immediately after the loop in the program is executed.

cnt = 0
while(cnt < 3):
    cnt = cnt+1
    print("Hello gfg")
else:
    print("Inside else block")

# while True:
#     print("Universaly true")
    
# Nested Loops

# Python programming language allows to use one loop inside another loop which is called nested loop. Following section shows few examples to illustrate the concept. 

for i in range(1,5):
    for j in range(i):
        print(j , end=' ')
    print()

#Continue
for i in "geeksforgeeks":
    if i == 'e' or i == 's':
        continue
    print(i , end=' ')

#Break
for i in "geeksforgeeks":
    if i == 'e' or i == 's':
        break
    
print("\nCurrent letter",i)

#Pass : We use pass statement in Python to write empty loops. Pass is also used for empty control statements, functions and classes.
for letter in 'geeksforgeeks':
    pass
print('Last Letter :', letter)
