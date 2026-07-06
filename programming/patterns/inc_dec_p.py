n=int(input())
print("-------------j decrement----------------------")
for i in range(1,n+1):
    for j in range(n,0,-1):
        print(f"{i}{j}",end=" ")
    print()
# 15 14 13 12 11 
# 25 24 23 22 21 
# 35 34 33 32 31 
# 45 44 43 42 41 
# 55 54 53 52 51 
print("-------------i and j decrement----------------------")
for i in range(n,0,-1):
    for j in range(n,0,-1):
        print(f"{i}{j}",end=" ")
    print()
# 55 54 53 52 51 
# 45 44 43 42 41 
# 35 34 33 32 31 
# 25 24 23 22 21 
# 15 14 13 12 11 
print("---------------i decrement----------------------")
for i in range(n,0,-1):
    for j in range(1,n+1):
        print(f"{i}{j}",end=" ")
    print()
# 51 52 53 54 55 
# 41 42 43 44 45 
# 31 32 33 34 35 
# 21 22 23 24 25 
# 11 12 13 14 15 
print("----------------------------------------------")
for i in range(n,0,-1):
    for j in range(n,0,-1):
        if i>=j:
            print(i,end=" ")
        else:
            print(j,end=" ")
    print()
# 5 5 5 5 5 
# 5 4 4 4 4 
# 5 4 3 3 3 
# 5 4 3 2 2 
# 5 4 3 2 1 
print("----------------------------------------------")
c=65
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(c),end=" ")
        c=c+1
    print()
# A B C D E 
# F G H I J 
# K L M N O 
# P Q R S T 
# U V W X Y 