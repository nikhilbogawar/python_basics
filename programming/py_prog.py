# finding average
# a = int(input())
# b = int(input())
# sum = 0
# c = 0
# for i in range(a, b+1):
#     sum = sum + i
#     c = c + 1
# avg = sum / c
# print("%.2f"%avg)
# ------------------------------------------------------------------------
# find average from even numbers
# a = int(input())
# b = int(input())
# sum = 0
# c = 0
# for i in range(a, b+1):
#     if i%2==0 :
#         sum = sum + i
#         c = c + 1
# avg = sum / c
# print("%.2f"%avg)
# ------------------------------------------------------------------------
# print even numbers another method
# a=5
# b=9
# if a%2==1 :
#     a=a+1
# for i in range(a,b+1,2):
#     print(i)
# ------------------------------------------------------------------------
# print alternative even numbers
# a=5
# b=20
# if a%2==1 :
#     a=a+1
# for i in range(a,b+1,4):
#     print(i)
# ------------------------------------------------------------------------
# print alternative even numbers total sum
# a=10
# b=25
# c=sum=0
# for i in range(a,b+1):
#     if i%2==0 :
#        c=c+1
#        if c%2==1 :
#            sum = sum+i
# print(sum) 
# ------------------------------------------------------------------------
# alternative even numbers of average
# a=10
# b=25
# c=sum=c1=0
# for i in range(a,b+1):
#     if i % 2 ==0:
#         c=c+1
#         if c%2==1:
#             sum=sum+i
#             c1=c1+1
# print(sum/c1)
# ------------------------------------------------------------------------
# print ABABAB but when you give n=7 it should print like ABABABA
# n=15
# for i in range(1,n+1):
#     if i%2==0:
#         print("B", end=" ")
#     else:
#         print("A", end=" ")
# ------------------------------------------------------------------------
# print ABCABCAB....
# n=15
# for i in range(1,n+1):
#     if (i%3==1):
#         print("A", end=" ")
#     elif (i%3==2):
#         print("B", end=" ")
#     else:
#         print("C", end=" ")
# ------------------------------------------------------------------------    
# Write a program to print all numbers which are divisible by 11 in given range if no such numbers print NO NUMBERS if starting range is greater than ending range then print INVALID RANGE
# n=int(input())
# n1=int(input())
# if n>n1:
#     print("INVALID RANGE")
# else:
#     c=0
#     for i in range(n,n1+1):
#         if i%11==0:
#             print(i, end=" ")
#             c=+1
#     if c==0:
#         print("NO NUMBERS")
# ------------------------------------------------------------------------    
# a=int(input())
# b=int(input())
# c=0
# if a>b:
#     a,b=b,a
# for i in range(a,b+1):
#     c=c+1
#     if (c>1):
#         print(end=",")
#     print(f"{i}*{i+1}", end=" ")
# print()
# c=0
# for i in range(a,b+1):
#     c=c+1
#     if (c>1):
#         print(end=",")
#     print(i*(i+1), end=" ")
# output: 
# 1*2 ,2*3 ,3*4 ,4*5 ,5*6 ,6*7 ,7*8 ,8*9 ,9*10 ,10*11 
# 2 ,6 ,12 ,20 ,30 ,42 ,56 ,72 ,90 ,110 
# ------------------------------------------------------------------------    
# alternative even numbers of its average:
# a=int(input("enter the first number:"))
# b=int(input("enter teh second number:"))
# c=sum=0
# if a%2==0:
#     q=a+2
# else:
#     q=a+1
# for i in range(q,b,4):
#     if i%2==0:
#         c=c+1
#         sum=sum+i
# print("average of the alternative even number is:",int(sum/c))
#------------------------------------------------------------------------
a = float(input())
b= float(input())
c=0
while(round(a,1)<=b):
   c=c+1
   if c>1:
       print(end=", ")
   print(f"{a:.1f}^2",end="")
   a=a+0.2
print(".")
        