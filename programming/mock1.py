# Write a program to print the number which is maximum and less than given number and such that the number must contain given digit and it must greater than zero
a=int(input())
b=int(input())
c=a-1
while c>0:
    t=c
    while t>0:
        if t%10==b:
            print(c)
            exit()
        t//=10
    c-=1

# Write a Progrm to Print following Series?  If the user Given Value is 10 then we have to print ten terms like this 1, A, @, 1, A, @, 1, A, @, 1
n=int(input())
if n==0:
    print("Zero")
else:
    c=0
    n=abs(n)
    for i in range(1,n+1):
        c=c+1
        if c>1:
            print(end=", ")
        if i%3==1:
            print("1",end="")
        elif i%3==0:
            print("@",end="")
        else:
            print("A",end="")
            
# Write a program to find Average of all Alternative Prime Numbers between The Given Values.
a=int(input())
b=int(input())
if a<=0 or b<=0:
    print("Invalid Inputs")
else:
    if a>b:
        a,b=b,a
    sum=0
    c=0
    ac=0
    for i in range(a+1,b):
        fc=0
        for j in range(1,i+1):
            if i%j==0:
                fc=fc+1
        if fc==2:
            ac=ac+1
            if ac%2==1:
                sum=sum+i
                c=c+1
    if c==0:
        print("No Prime Numbers")
    else:
        print("%.3f"%(sum/c))

# Write a program to print Fibonacci Series in the Given Range.
n=int(input())
n1=int(input())
a,b=0,1
count=0
if n>n1:
    n,n1=n1,n
if n>=0 and n1>=0:
    while(a<=n1):
        if(a>=n):
            print(a,end=" ")
            count=count+1
        c=a+b
        a=b
        b=c
    if count==0:
        print("No Fibonacci Series Values")
else:
    print("Invalid Inputs")

# Write a program to print given number is Harshad Number or not.
# Harshad number is a number which exactly divisible by the sum of its digits.
n=int(input())
sum=0
if n==0:
    print("Zero")
else:
    n=abs(n)
    t=n
    while(n>0):
        r=n%10
        sum=sum+r
        n=n//10
    if t%sum==0:
        print(sum)
        print("Harshad number")
    else:
        print(sum)
        print("not a Harshad number")