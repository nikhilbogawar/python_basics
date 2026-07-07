n=int(input())
for i in range(1,n+1):
    # for j in range(1,n+1):
    #     if i<=j:
    #         print("*",end=" ")
    # print()
    for j in range(1,n-i+2):
        print(end="*")
    print()
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 
print("------------------------------------")
for i in range(1,n+1):
    # for j in range(1,n+1):
    #     if i>=j:
    #         print("*",end=" ")
    # print()
    for j in range(1,i+1):
        print("*",end=" ")
    print()
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
print("------------------------------------")
for i in range(1,n+1):
    # for j in range(1,n+1):
    #     if i<=j:
    #         print("*",end=" ")
    #     else:
    #         print(" ",end=" ")
    # print()
    for j in range(1,i):
        print(end=" ")
    for j in range(1,n-i+2):
        print(end="*")
    print()
# * * * * * 
#   * * * * 
#     * * * 
#       * * 
#         * 
print("------------------------------------")
for i in range(1,n+1):
    # for j in range(1,n+1):
    #     if i+j>=n+1:
    #         print("*",end=" ")
    #     else:
    #         print(" ",end=" ")
    # print()
    for j in range(1,n-i+1):
        print(end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
#         * 
#       * * 
#     * * * 
#   * * * * 
# * * * * *
print("------------------------------------")
c=65
for i in range(1,n+1):
    for j in range(1,n+1):
        if i>=j:
            print(chr(c),end=" ")
            c=c+1
    print()
# A 
# B C 
# D E F 
# G H I J 
# K L M N O 