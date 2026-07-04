# 1*2*3*4*5
# 6*7*8*9*10
# 11*12*13*14*15
# 16*17*18*19*20
# 21*22*23*24*25
r=int(input())
c=int(input())
count=0
for i in range(1,r+1):
    d=0
    for j in range(1,c+1):
        count+=1
        d+=1
        if d>1:
            print(end="*")
        print(count,end="")
    print()
print("----------------------------------------")
# * * * * * 
# * $ $ $ * 
# * $ $ $ * 
# * $ $ $ * 
# * * * * * 
for i in range(1,r+1):
    for j in range(1,c+1):
        if i==1 or i==r or j==1 or j==c:
            print("*",end=" ")
        elif j==1 or j==c:
            print("*",end=" ")
        else:
            print("$",end=" ")
    print()
print("----------------------------------------")
# 5 5 5 5 5 
# 5 4 4 4 4 
# 5 4 3 3 3 
# 5 4 3 2 2 
# 5 4 3 2 1 
for i in range(1,r+1):
    for j in range(1,r+1):
        if i==j:
            print((r+1)-j,end=" ")
        elif i>j:
            print((r+1)-j,end=" ")
        else:
            print((r+1)-i,end=" ")
    print()