n=int(input())
print("-----------------------------------")
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print("*",end=" ")
        else:
            print(end="  ")
    print()
# * * * * * 
# *       * 
# *       * 
# *       * 
# * * * * * 
print("------------------------------------")
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        if i==n or j==1 or i==j:
            print("*",end=" ")
        else:
            print(end="  ")
    print()
#     * 
#    * * 
#   *   * 
#  *     * 
# * * * * * 
print("---------------------------------------")
for i in range(n,0,-1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        if i==n or j==1 or i==j:
            print("*",end=" ")
        else:
            print(end="  ")
    print()
# * * * * * 
#  *     * 
#   *   * 
#    * * 
#     * 
print("----------------------------------------")
for i in range(1,n+1):
    print("  "*(n-i),end="")
    for j in range(1,i+1):
        if i==n or j==1 or i==j:
            print("*",end=" ")
        else:
            print(end="  ")
    print()
#         * 
#       * * 
#     *   * 
#   *     * 
# * * * * * 
print("----------------------------------------")
for i in range(n,0,-1):
    print("  "*(n-i),end="")
    for j in range(1,i+1):
        if i==n or j==1 or i==j:
            print("*",end=" ")
        else:
            print(end="  ")
    print()
# * * * * * 
#   *     * 
#     *   * 
#       * * 
#         * 
print("----------------------------------------")
for i in range(1,n+1):
    for j in range(1,i+1):
        if i==n or j==1 or i==j:
            print("*",end=" ")
        else:
            print(end="  ")
    print()
# * 
# * * 
# *   * 
# *     * 
# * * * * * 
print("----------------------------------------")
for i in range(n,0,-1):
    for j in range(1,i+1):
        if i==n or j==1 or i==j:
            print("*",end=" ")
        else:
            print(end="  ")
    print()
# * * * * * 
# *     * 
# *   * 
# * * 
# * 