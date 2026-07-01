# factors of a number:
# n=int(input())
# for i in range(1,n+1):
#     if n%i==0:
#         print(i,end=" ")

# factors count and sum and average:
# n=int(input())
# c=sum=0
# for i in range(1,n+1):
#     if n%i==0:
#         c=c+1
#         sum=sum+i
# print("Average:",sum/c)
# print("Sum:",sum)
# print("Count:",c)

# print prime numbers:
# n=int(input())
# c=0
# for i in range(1,n+1):
#     if n%i==0:
#         c=c+1
# if c==2:
#     print(i)

# prime numbers in a given range:
# a=int(input())
# b=int(input())
# for i in range(a,b+1):
#     fc=0
#     for j in range(1,i+1):
#         if i%j==0:
#             fc=fc+1
#     if fc==2:
#         print(i,end=" ")

# sum of prime numbers in a given range:
# a=int(input())
# b=int(input())
# sum=0
# for i in range(a,b+1):
#     fc=0
#     for j in range(1,i+1):
#         if i%j==0:
#             fc=fc+1
#     if fc==2:
#         sum=sum+i
# print(sum)

# average of prime numbers in a given range:
# a=int(input())
# b=int(input())
# sum=0
# c=0
# for i in range(a,b+1):
#     fc=0
#     for j in range(1,i+1):
#         if i%j==0:
#             fc=fc+1
#     if fc==2:
#         c=c+1
#         sum=sum+i
# print(int(sum/c))

# alternative of prime numbers in a given range:
# a=int(input())
# b=int(input())
# ac=0
# for i in range(a,b+1):
#     fc=0
#     for j in range(1,i+1):
#         if i%j==0:
#             fc=fc+1
#     if fc==2:
#         ac=ac+i
#         if ac%2==1:
#             print(i)
       
# alternative prime numbers sum, count, average in a given range     
# a=int(input("Enter the first number:"))
# b=int(input('Enter the second number:'))
# ac=0
# c=0
# sum=0
# for i in range(a,b+1):
#     fc=0
#     for j in range(1,i+1):
#         if i%j==0:
#             fc=fc+1
#     if fc==2:
#         ac=ac+i
#         if ac%2==1:
#             c=c+1
#             sum=sum+i
#             print("Count:",c,end=" ")
#             print("Sum:",sum,end=" ")
#             print()
# print("Count:",c)
# print("Sum:",sum)
# print("Average:",sum/c)

# print N prime without using factor count
# n=int(input())
# c=0
# p=2
# if n<=0:
#     print("Invalid Input")
# else:
#     while(True):
#         b=True
#         for i in range(2,int(p**0.5)+1):
#             if p%i==0:
#                 b=False
#                 break
#         if b==True and p>1:
#             c+=1
#             if c>1:
#                 print(end=", ")
#             print(p,end="") 
#             if c==n:
#                 break 
#         p+=1

# print N prime numbers using factor count
# n=int(input("Enter the input:"))
# p=2
# c=0
# while(True):
#     fc=0
#     for i in range(1,p+1):
#         if p%i==0:
#             fc=fc+1
#     if fc==2:
#         print(p,end=" ")
#         c=c+1
#         if c==n:
#             break
#     p=p+1

# check if a given number is prime. If it is not prime, print "Not a prime number" and stop. If it is prime, find and print the nearest smaller and larger prime numbers, and then display the closest one.
n = int(input())
p = True
if n < 2:
    p = False
else:
    for i in range(2, n):
        if n % i == 0:
            p = False
            break

if p == False:
    print("Not a prime number")
else:
    low = n - 1
    while low > 1:
        a = True
        for i in range(2, low):
            if low % i == 0:
                a = False
                break
        if a == True:
            break
        low -= 1
    high = n + 1
    while True:
        a = True
        for i in range(2, high):
            if high % i == 0:
                a = False
                break
        if a == True:
            break
        high += 1
    print("Lowest near prime:", low)
    print("Highest near prime:", high)
    if (n - low) == (high - n):
        print("Nearest prime:", low, high)
    elif (n - low) <= (high - n):
        print("Nearest prime:", low)
    else:
        print("Nearest prime:", high)