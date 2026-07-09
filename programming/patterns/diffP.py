n=int(input())
print("-----------------------------------")
c=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(c,end=" ")
        c=c+1
    print()
# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 
# 11 12 13 14 15 
print("-----------------------------------")
c=2
for i in range(1,n+1):
    for j in range(1,i+1):
        print(c,end=" ")
        c=c+2
    print()
# 2 
# 4 6 
# 8 10 12 
# 14 16 18 20 
# 22 24 26 28 30 
print("-----------------------------------")
c=2
for i in range(1,n+1):
    for j in range(1,i+1):
        print(c,end=" ")
        c=c+2
    c=c-1
    print()
# 2 
# 3 5 
# 6 8 10 
# 11 13 15 17 
# 18 20 22 24 26 
print("-----------------------------------")
for i in range(1,n+1):
    for j in range(1,i+1):
        if i%2==1:
            print("*",end=" ")
        else:
            print("$",end=" ")
    print()
# * 
# $ $ 
# * * * 
# $ $ $ $ 
# * * * * * 
print("-----------------------------------")
c=1
for i in range(1,n+1):
    sum=0
    for j in range(1,i+1):
        print(c,end=" ")
        sum=sum+c
        c=c+2
    print(f"- {sum}")
# 1 - 1
# 3 5 - 8
# 7 9 11 - 27
# 13 15 17 19 - 64
# 21 23 25 27 29 - 125
print("------------------------------------")
for i in range(1,n+1):
    k=n+64
    for j in range(1,n-i+1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(chr(k),end=" ")
        k=k-1
    print()
#         E 
#       E D 
#     E D C 
#   E D C B 
# E D C B A 
print("-------------------------------------")
c=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(c,end=" ")
        if c==1:
            c=0
        else:
            c=1
    print()
# 1 
# 0 1 
# 0 1 0 
# 1 0 1 0 
# 1 0 1 0 1 
print("-------------------------------------")
c=0
for i in range(1,n+1):
    if i%2==0:
        d=c+i
    for j in range(1,i+1):
        c=c+1
        if i%2==1:
            print(c,end=" ")
        else:
            print(d,end=" ")
            d=d-1
    print()
# 1 
# 3 2 
# 4 5 6 
# 10 9 8 7 
# 11 12 13 14 15 
print("-------------------------------------")
c=0
for i in range(1,n+1):
    if i%2==0:
        d=c+i
    for j in range(1,i+1):
        c=c+1
        if j>1:
            print("*",end="")
        if i%2==1:
            print(c,end="")
        else:
            print(d,end="")
            d=d-1
    print()
# 1
# 3*2
# 4*5*6
# 10*9*8*7
# 11*12*13*14*15
print("--------------------------------------")
for i in range(1,n+1):
    k=i
    d=n-1
    for j in range(1,i+1):
        print(k, end=" ")
        k=k+d
        d=d-1
    print()
# 1 
# 2 6 
# 3 7 10 
# 4 8 11 13 
# 5 9 12 14 15 