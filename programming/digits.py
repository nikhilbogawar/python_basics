# accessing digits
# n=153
# while(n>0):
#     r=n%10
#     print(r,end="")
#     n=n//10 #351

# sum, count, and average of digits
# n=153
# sum=c=0
# while(n>0):
#     r=n%10
#     sum=sum+r
#     c=c+1
#     n=n//10
# print("Sum:",sum)  # 9
# print("Count:",c)  # 3
# print("Average:",sum/c)  # 3.0

# print even digits
# n=265
# while(n>0):
#     r=n%10
#     if r%2==0:
#         print(r,end=" ")    # 6 2
#     n=n//10
# ---- or -----
# n=265
# while(n>0):
#     r=n%10
#     if (r==2 or r==3 or r==5 or r==7):
#         print(r,end=" ")   # 6 2
#     n=n//10

# print highest digit
# n=153
# h=0
# while(n>0):
#     r=n%10
#     if r>h:
#         h=r
#     n=n//10
# print(h) # 5

# print smallest digit
# n=153
# s=9
# while(n>0):
#     r=n%10
#     if r<s:
#         s=r
#     n=n//10
# print(s)  # 1

#