n=int(input())
print("------------for *-------------")
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end="")
    print()
# *****
# *****
# *****
# *****
# *****
print("------------for i-------------")
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,end="")
    print()
# 11111
# 22222
# 33333
# 44444
# 55555
print("-----------for j--------------")
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end="")
    print()
# 12345
# 12345
# 12345
# 12345
# 12345
print("------------for diagonal 1's-------------")
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            print(1,end="")
        else:
            print(0,end="")
    print()
# 10000
# 01000
# 00100
# 00010
# 00001
print("------------for diagonal and lower left 1's-------------")
for i in range(1,n+1):
    for j in range(1,n+1):
        if i>=j:
            print(1,end="")
        else:
            print(0,end="")
    print()
# 10000
# 11000
# 11100
# 11110
# 11111
print("------------for diagonal and higher right 1's-------------")
for i in range(1,n+1):
    for j in range(1,n+1):
        if i<=j:
            print(1,end="")
        else:
            print(0,end="")
    print()
# 11111
# 01111
# 00111
# 00011
# 00001
print("------------for diagonal 1's and higher right 0's and lower left 2's-------------")
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            print(1,end="")
        elif i>j:
            print(2,end="")
        else:
            print(0,end="")
    print()
# 10000
# 21000
# 22100
# 22210
# 22221
print("------------for opposite diagonal 0's-------------")
for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j==n+1:
            print(0,end="")
        else:
            print(1,end="")
    print()
# 11110
# 11101
# 11011
# 10111
# 01111
print("------------for opposite diagonal 1's and higher left 2's and lower right 1's-------------")
for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j<n+1:
            print(2,end="")
        elif i+j==n+1:
            print(0,end="")
        else:
            print(1,end="")
    print()
# 22220
# 22201
# 22011
# 20111
# 01111
print("----------------------------------------------")
if n%2==0:
    for i in range(1,n+1):
        for j in range(1,n+1):
            if (i+j)%2==0:
                print("1",end=" ")
            else:
                print("0",end=" ")
        print()
# 1 0 1 0 1 0       input must be even i have given input as 6
# 0 1 0 1 0 1 
# 1 0 1 0 1 0 
# 0 1 0 1 0 1 
# 1 0 1 0 1 0 
# 0 1 0 1 0 1 