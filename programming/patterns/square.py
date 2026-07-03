n=int(input())
print("------------for *-------------")
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end="")
    print()
print("------------for i-------------")
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,end="")
    print()
print("-----------for j--------------")
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end="")
    print()
print("------------for diagonal 1's-------------")
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            print(1,end="")
        else:
            print(0,end="")
    print()
print("------------for diagonal and lower left 1's-------------")
for i in range(1,n+1):
    for j in range(1,n+1):
        if i>=j:
            print(1,end="")
        else:
            print(0,end="")
    print()
print("------------for diagonal and higher right 1's-------------")
for i in range(1,n+1):
    for j in range(1,n+1):
        if i<=j:
            print(1,end="")
        else:
            print(0,end="")
    print()
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
print("------------for opposite diagonal 0's-------------")
for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j==n+1:
            print(0,end="")
        else:
            print(1,end="")
    print()
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