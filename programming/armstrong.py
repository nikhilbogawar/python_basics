# print the number is armstrong or not
# n=153
# dc=0
# sum=0
# temp=n
# while(temp>0):
#     dc=dc+1
#     temp=temp//10
# temp=n
# while(temp>0):
#     r=temp%10
#     sum=sum+(r**dc)
#     temp=temp//10
# if sum==n:
#     print("Armstrong Number")   # print(n)
# else:
#     print("Not a Armstrong Number")

# print armstrong number, its sum, its count, average in a given range
a=int(input())
b=int(input())
c=0
sum=0
for i in range(a,b+1):
    dc=arm=0
    temp=i
    while(temp>0):
        dc=dc+1
        temp=temp//10
    temp=i
    while(temp>0):
        r=temp%10
        arm=arm+(r**dc)
        temp=temp//10
    if arm==i:
        print("Armstrong Numbers Are:",i)
        sum=sum+i
        c=c+1
print("Sum of all armstrong numbers:",sum)
print("Count of all armstrong numbers:",c)
print("Average of all armstrong numbers:",sum//c)