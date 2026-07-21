n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==1 or i==1 or i==n:
            print("*",end=" ")
        else:
            print(end="  ")
    print(" ",end="")
    for j in range(1,n+1):
        if j==1 or j==n or i==n//2+1:
            print("*",end=" ")
        else:
            print(end="  ")
    print(" ",end="")
    for j in range(1,n+1):
        if j==1 or i==1 or j==n or i==n//2+1:
            print("*",end=" ")
        else:
            print(end="  ")
    print(" ",end="")
    for j in range(1,n+1):
        if i==1 or i==n or j==n//2+1:
            print("*",end=" ")
        else:
            print(end="  ")
    print(" ",end="")
    for j in range(1,n+1):
        if i==1 or j==n//2+1:
            print("*",end=" ")
        else:
            print(end="  ")
    print(" ",end="")
    for j in range(1,n+1):
        if j==1 or j==n or i==n:
            print("*",end=" ")
        else:
            print(end="  ")
    print(" ",end="")
    for j in range(1,n+1):
        if j==1 or j==n or i==n:
            print("*",end=" ")
        else:
            print(end="  ")
    print()
# * * * * *  *       *  * * * * *  * * * * *  * * * * *  *       *  *       * 
# *          *       *  *       *      *          *      *       *  *       * 
# *          * * * * *  * * * * *      *          *      *       *  *       * 
# *          *       *  *       *      *          *      *       *  *       * 
# * * * * *  *       *  *       *  * * * * *      *      * * * * *  * * * * * 