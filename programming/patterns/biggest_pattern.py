n=int(input())
for i in range(1,n+1):
    if n<=9:
        print(" "*(n-i),end="")
    else:
        print("  "*(n-i),end="")
    for j in range(1,i+1):
        if n<=9:
            print(i,end=" ")
        else:
            if i<=9:
                print(end=" ")
            print(i,end="  ")
    print()
for i in range(n-1,0,-1):
    if n<=9:
        print(" "*(n-i),end="")
    else:
        print("  "*(n-i),end="")
    for j in range(1,i+1):
        if n<=9:
            print(i,end=" ")
        else:
            if i<=9:
                print(end=" ")
            print(i,end="  ")
    print()
# output if input is 14
#                            1  
#                          2   2  
#                        3   3   3  
#                      4   4   4   4  
#                    5   5   5   5   5  
#                  6   6   6   6   6   6  
#                7   7   7   7   7   7   7  
#              8   8   8   8   8   8   8   8  
#            9   9   9   9   9   9   9   9   9  
#         10  10  10  10  10  10  10  10  10  10  
#       11  11  11  11  11  11  11  11  11  11  11  
#     12  12  12  12  12  12  12  12  12  12  12  12  
#   13  13  13  13  13  13  13  13  13  13  13  13  13  
# 14  14  14  14  14  14  14  14  14  14  14  14  14  14  
#   13  13  13  13  13  13  13  13  13  13  13  13  13  
#     12  12  12  12  12  12  12  12  12  12  12  12  
#       11  11  11  11  11  11  11  11  11  11  11  
#         10  10  10  10  10  10  10  10  10  10  
#            9   9   9   9   9   9   9   9   9  
#              8   8   8   8   8   8   8   8  
#                7   7   7   7   7   7   7  
#                  6   6   6   6   6   6  
#                    5   5   5   5   5  
#                      4   4   4   4  
#                        3   3   3  
#                          2   2  
#                            1  
# output if input is 5
#     1 
#    2 2 
#   3 3 3 
#  4 4 4 4 
# 5 5 5 5 5 
#  4 4 4 4 
#   3 3 3 
#    2 2 
#     1 