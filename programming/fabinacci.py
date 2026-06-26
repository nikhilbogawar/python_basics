# find factoria of a given number
# n=int(input())
# fact=1
# if n>0:
#     for i in range(1,n+1):
#         fact=fact*i
#     print(fact)
# else:
#     print("Invalid Input")

# to print the average of the alternative finonacci series in the given range
# n=int(input())
# n1=int(input())
# a,b=0,1
# ac=0
# sum=count=0
# if n>n1:
#     n,n1=n1,n
# if n>=0 and n1>=0:
#     while a<=n1:
#         if a>=n:
#             ac=ac+1
#             if ac%2==1:
#                 sum=sum+a
#                 count=count+1
#         c=a+b
#         a=b
#         b=c
#     if count==0:
#         print("No Fibonacci Series")
#     else:
#         print("%.2f"%(sum/count))
# else:
#     print("Invalid Inputs")

# to print first N terms of Alternative Fibonacci Series
# n=int(input())
# a,b=0,1
# ac=0
# if n<0:
#     n=-(n)
# if n==0:
#     print("Invalid Input")
# else:
#     for i in range(1,(n*2)+1):
#         ac=ac+1
#         if ac%2==1:
#             if ac>2:
#                 print(end=", ")
#             print(a,end="")
#         c=a+b
#         a=b
#         b=c

# print the average of the fibonacci series in between the given range
# n=int(input())
# n1=int(input())
# a,b=0,1
# sum=0
# count=0
# if a>=0 and b>=0:
#     while(a<=n1):
#         if a>=n:
#             sum=sum+a
#             count=count+1
#         c=a+b
#         a=b
#         b=c
#     if count==0:
#         print("No Fibonacci Series")
#     else:
#         print("%.2f"%(sum/count))
# else:
#     print("Invalid Inputs")


# print fibonacci series in the given range
# n=int(input())
# n1=int(input())
# a,b=0,1
# count=0
# if n>n1:
#     n,n1=n1,n
# if a>=0 and b>=0:
#     while(a<=n1):
#         if a>=n:
#             print(a,end=" ")
#             count=count+1
#         c=a+b
#         a=b
#         b=c
#     if count==0:
#         print("No Fibonacci Series")
# else:
#     print("Invalid Inputs")


# print fibonacci series between in the given range
# n=int(input())
# n1=int(input())
# a,b=0,1
# count=0
# if n>n1:
#     n,n1=n1,n
# if a>=0 and b>=0:
#     while(a<n1):
#         if a>n:
#             print(a,end=" ")
#             count=count+1
#         c=a+b
#         a=b
#         b=c
#     if count==0:
#         print("No Fibonacci Series")
# else:
#     print("Invalid Inputs")


# print first N terms in the fibonacci series
# n=int(input())
# a,b=0,1
# if n<0:
#     n=-(n)
# if n==0:
#     print("Invalid Input")
# else:
#     for i in range(1,n+1):
#         print(a,end=" ")
#         c=a+b
#         a=b
#         b=c
        
# find sum of factorials upto N numbers like 0! + 1! + 2! +... upto n!?
# n=int(input())
# if n>=0:
#     fact=1
#     sum=1
#     print(1,end="")
#     for i in range(1,n+1):
#         fact=fact*i
#         sum=sum+fact
#         print("+",end="")
#         print(fact,end="")
#     print("=",end="")
#     print(sum)
# else:
#     print("Invalid Input")

# print the sum of the fibonacci series of first N terms
# n=int(input())
# a,b=0,1
# sum=0
# if n>0:
#     for i in range(1,n+1):
#         sum=sum+a
#         c=a+b
#         a=b
#         b=c
#     print(sum)
# else:
#     print("Invalid Input")

# check weather the given input is a fibonacci number or not
# n=int(input())
# a,b=0,1
# while a<n:
#     c=a+b
#     a=b
#     b=c
# if a==n:
#     print("The Given Number is a Fibonacci")
# else:
#     print("The Given Number is not a Fibonacci")