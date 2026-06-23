# print count number of the digits in a given number
# n=int(input())
# c=0
# if n==0:
#     print("Invalid Input")
# else:
#     if n>0:
#         while(n>0):
#             c=c+1
#             n=n//10
#         if c==1:
#             print("Given Number consists of only 1 digit.")
#         else:
#             print(f"given number consists of {c} digits.")
#     elif n<0:
#         n=-(n)
#         while(n>0):
#             c=c+1
#             n=n//10
#         if c==1:
#             print("given number consists of only 1 digit but it is a negative value.")
#         else:
#             print(f"given number consists of {c} digits but it is a negative value.")

# print the highest digit in a given number
# n=int(input())
# h=0
# if n>0:
#     while(n>0):
#         r=n%10
#         if r>h:
#             h=r
#         n=n//10
#     print(f"Highest digit in a given number is {h}.")
# else:
#     print("Invalid Input")  

# print the smallest digit in a given number
# n=int(input())
# s=9
# if n>0:
#     while(n>0):
#         r=n%10
#         if r<s:
#             s=r
#         n=n//10
#     print(f"Smallest digit of a given number is {s}.")
# else:
#     print("Invalid Input")        

# find sum of first 'n' natural numbers by using formula
# n=int(input())
# if n<0:
#     print("Sorry! you have entered negative values") 
# elif n==0:
#     print("Invalid Input")
# else:
#     total=n*(n+1)//2
#     print(f"sum of 'n' natural numbers is {total}")

# print sum of 'n' natural numbers without using formula
# n=int(input())
# c=0
# if n==0:
#     print("InvaLid Input.")
# elif n<0:
#     print("Sorry! you have Entered Negative Values.")
# else:
#     sum=0
#     a=""
#     for i in range(1,n+1):
#         sum=sum+i
#         c=c+1
#         if c==1:
#             print(f"Sum of 'N' Natural Numbers is ",end="")
#         if c>1:
#             print(end=" + ")
#         print(i,end="")
#     print(f" = {sum}.")

# print the sum of the even digits in a given number
# n=int(input())
# sum=0
# if n>0:
#     while(n>0):
#         r=n%10
#         if r%2==0:
#             sum=sum+r
#         n=n//10
#     print(sum)
# else:
#     print("Invalid Input")

# print the number is a perfrect square or not
# n=int(input())
# if n<=0:
#     print("Invlaid Input")
# else:
#     i=1
#     while i*i<n:
#         i=i+1
#     if i*i==n:
#         print("Perfect Square")
#     else:
#         print("Not a perfect square")
        
# print sum of odd positions in a given number
# n=int(input())
# sum=0
# c=0
# if n<=0:
#     print("Invalid Input")
# else:
#     while(n>0):
#         r=n%10
#         if c%2==0:
#             sum=sum+r
#         c=c+1
#         n=n//10
#     print(sum)

# print sum of digits of a number
# n=int(input())
# c=0
# if n<=0:
#     print("Invalid Input")
# else:
#     rev=0
#     t=n
#     while t>0:
#         r=t%10
#         rev=rev*10+r
#         t=t//10
#     while rev>0:
#         r=rev%10
#         rev=rev//10
#         c=c+1
#         if c>1:
#             print(end=" + ")
#         print(r,end="")
#     print(".")