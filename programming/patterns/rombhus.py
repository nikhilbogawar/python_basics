n=int(input())
print("---------------------------------------------------")
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(end="* ")
    print()
for i in range(n-1,0,-1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(end="* ")
    print() 
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     * 
print("---------------------------------------------------")
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(i,end=" ")
    print()
for i in range(n-1,0,-1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(i,end=" ")
    print() 
#     1 
#    2 2 
#   3 3 3 
#  4 4 4 4 
# 5 5 5 5 5
#  4 4 4 4 
#   3 3 3 
#    2 2 
#     1 
print("---------------------------------------------------")
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(j,end=" ")
    print()
for i in range(n-1,0,-1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(j,end=" ")
    print()
#     1 
#    1 2 
#   1 2 3 
#  1 2 3 4 
# 1 2 3 4 5 
#  1 2 3 4 
#   1 2 3 
#    1 2 
#     1 
print("---------------------------------------------------")
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(j,end="")
    for j in range(i-1,0,-1):
        print(j,end="")
    print()
for i in range(n-1,0,-1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(j,end="")
    for j in range(i-1,0,-1):
        print(j,end="")
    print()
#     1
#    121
#   12321
#  1234321
# 123454321
#  1234321
#   12321
#    121
#     1
print("---------------------------------------------------")
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(i,0,-1):
        print(j,end="")
    for j in range(2,i+1):
        print(j,end="")
    print()
for i in range(n-1,0,-1):
    print(" "*(n-i),end="")
    for j in range(i,0,-1):
        print(j,end="")
    for j in range(2,i+1):
        print(j,end="")
    print()
#     1
#    212
#   32123
#  4321234
# 543212345
#  4321234
#   32123
#    212
#     1
print("---------------------------------------------------")
for i in range(1,n+1):
    k=1
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(k,end=" ")
        k=k*(i-j)//j
    print()
for i in range(n-1,0,-1):
    k=1
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(k,end=" ")
        k=k*(i-j)//j
    print()
#     1 
#    1 1 
#   1 2 1 
#  1 3 3 1 
# 1 4 6 4 1 
#  1 3 3 1 
#   1 2 1 
#    1 1 
#     1 
print("---------------------------------------------------")
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(end="0 ")
    print()
for i in range(n-1,0,-1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(end="0 ")
    print() 
#     0 
#    0 0 
#   0 0 0 
#  0 0 0 0 
# 0 0 0 0 0 
#  0 0 0 0 
#   0 0 0 
#    0 0 
#     0 