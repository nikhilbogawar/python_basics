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
print("------------------------------------------")
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        if i==j or j==1:
            print("*",end=" ")
        else:
            print(end="  ")
    print()
for i in range(n-1,0,-1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        if i==j or j==1:
            print("*",end=" ")
        else:
            print(end="  ")
    print()
#     * 
#    * * 
#   *   * 
#  *     * 
# *       * 
#  *     * 
#   *   * 
#    * * 
#     * 
print("-----------------------------------")
for i in range(n,0,-1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print(" "*(n-i),end="")
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(2,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print(" "*(n-i),end="")
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
# * * * * * * * * * * 
#  * * * *   * * * * 
#   * * *     * * * 
#    * *       * * 
#     *         * 
#    * *       * * 
#   * * *     * * * 
#  * * * *   * * * * 
# * * * * * * * * * * 
print("----------------------------------")
for i in range(n,0,-1):
    print(" "*(n-i),end="")
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print("*",end=" ")
        else:
            print(end="  ")
    print()
# * * * * * 
#  *       * 
#   *       * 
#    *       * 
#     * * * * * 
print("-----------------------------------")
for i in range(n,0,-1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        if j==1 or i==n or i==j:
            print("*",end=" ")
        else:
            print(end="  ")
    print()
for i in range(2,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        if j==1 or i==n or i==j:
            print("*",end=" ")
        else:
            print(end="  ")
    print()
# * * * * * 
#  *     * 
#   *   * 
#    * * 
#     * 
#    * * 
#   *   * 
#  *     * 
# * * * * * 
print("------------------------------------")
for i in range(1,n+1):
    print(" "*n+" "*(n-i),end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print(" "*(n-i),end="")
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
#          * 
#         * * 
#        * * * 
#       * * * * 
#      * * * * * 
#     *         * 
#    * *       * * 
#   * * *     * * * 
#  * * * *   * * * * 
# * * * * * * * * * * 
print("--------------------------------------")
for i in range(1,n+1):
    print("  "*(n-i),end="")
    for j in range(1,i+1):
        if j==1 or i==j:
            print("*",end=" ")
        else:
            print(end="  ")
    print()
for i in range(n-1,0,-1):
    print("  "*(n-i),end="")
    for j in range(1,i+1):
        if j==1 or i==j:
            print("*",end=" ")
        else:
            print(end="  ")
    print()
#         * 
#       * * 
#     *   * 
#   *     * 
# *       * 
#   *     * 
#     *   * 
#       * * 
#         * 
print("-------------------------------------")
c=1
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print(f"{c:02d}",end=" ")
            c=c+1
        else:
            print(end="   ")
    print()
# 01 02 03 04 05 
# 06          07 
# 08          09 
# 10          11 
# 12 13 14 15 16 
