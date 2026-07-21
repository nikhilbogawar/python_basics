n=int(input())
# for i in range(1,n+1):
#     for j in range(1,n-i+2):
#         print(j,end=" ")
#     print("    "*(i-1),end="")
#     if i==1:
#         for j in range(2,n-i+2):
#             print(n-i-j+2,end=" ")
#     else:
#         for j in range(1,n-i+2):
#             print(n-i-j+2,end=" ")
#     print()
# for i in range(n-1,0,-1):
#     for j in range(1,n-i+2):
#         print(j,end=" ")
#     print("    "*(i-1),end="")
#     if i==1:
#         for j in range(2,n-i+2):
#             print(n-i-j+2,end=" ")
#     else:
#         for j in range(1,n-i+2):
#             print(n-i-j+2,end=" ")
#     print()



for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    if i<n:
        print("  "*(2*(n-i)-1),end="")
    if i==n:
        for j in range(n-1,0,-1):
            print(j,end=" ")
    else:
        for j in range(i,0,-1):
            print(j,end=" ")
    print()
for i in range(2,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    if i<n:
        print("  "*(2*(n-i)-1),end="")
    if i==n:
        for j in range(n-1,0,-1):
            print(j,end=" ")
    else:
        for j in range(i,0,-1):
            print(j,end=" ")
    print()
# 1 2 3 4 5 4 3 2 1 
# 1 2 3 4   4 3 2 1 
# 1 2 3       3 2 1 
# 1 2           2 1 
# 1               1 
# 1 2           2 1 
# 1 2 3       3 2 1 
# 1 2 3 4   4 3 2 1 
# 1 2 3 4 5 4 3 2 1 