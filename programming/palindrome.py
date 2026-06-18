# reverse of a number
# n=153
# rev=0
# while(n>0):
#     r=n%10
#     rev=rev*10+r
#     n=n//10
# print(rev)    #351

# palindrome or not check
# n=153
# temp=n
# rev=0
# while(n>0):
#     r=n%10
#     rev=rev*10+r
#     n=n//10
# if rev==temp:
#     print("Palindrome")  # we can write as print(temp)  or print(rev) if it is palindrome numner
# else:
#     print("Not a Palindrome")

# check the number is palindrome or not in a given range
# a=int(input())
# b=int(input())
# for i in range(a,b+1):
#     temp=i
#     rev=0
#     while(i>0):
#         r=i%10
#         rev=rev*10+r
#         i=i//10
#     if rev==temp:
#         print(temp,end=" ")

# sum, count and average of a palindrome number in a range
# a=int(input())
# b=int(input())
# sum=c=0
# for i in range(a,b+1):
#     temp=i
#     rev=0
#     while(i>0):
#         r=i%10
#         rev=rev*10+r
#         i=i//10
#     if rev==temp:
#         sum=sum+temp
#         c=c+1
# print("Sum:",sum)
# print("Count:",c)
# print("Average:",sum/c)

# print alternative palindrome of sum count and average in the range
# a=int(input("Enter the first input:"))
# b=int(input("Enter the second input:"))
# sum=c=ac=0
# for i in range(a,b+1):
#     temp=i
#     rev=0
#     while(i>0):
#         r=i%10
#         rev=rev*10+r
#         i=i//10
#     if rev==temp:
#         ac=ac+1
#         if ac%2==1:
#             print(temp,end=" ")
#             sum=sum+temp
#             c=c+1
# print("Sum:",sum)
# print("Count:",c)
# print("Average:",sum/c)