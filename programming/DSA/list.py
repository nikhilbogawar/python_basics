# Insert into list
# l=list(map(int,input().split()))
# n=int(input())
# i=int(input())
# l.insert(i,n)
# print(*l)


# Merging two lists
# l1=list(map(int,input().split()))
# l2=list(map(int,input().split()))
# l3=l+l2
# print(*l3)


# Remove an element from the list
# l=list(map(int,input().split()))
# n=int(input())
# if n in l:
#     l.remove(n)
#     print(*l)
# else:
#     print("Invalid Input")


# Removing an element using specific index
# l=list(map(int,input().split()))
# i=int(input())
# n=l.pop(i)
# print(*l)


# By using Index Value find the value
# l=list(map(int,input().split()))
# n=int(input())
# if n in l:
#     i=l.index(n)
#     print(i)
# else:
#     print("Invalid Input")


# Count how many specific value elements are there in list
# l=list(map(int,input().split()))
# n=int(input())
# c=l.count(n)
# print(c)


# Print first and last element from the list
# l=list(map(int,input().split()))
# print(l[0]+l[-1])    # or print(l[0]+l[len(l)-1])


# Print upto specific element
# l=list(map(int,input().split()))
# i=int(input())
# for i in range(i+1):
#     print(l[i])


# Print sum upto a specific element
# l=list(map(int,input().split()))
# i=int(input())
# sum=0
# for i in range(i+1):
#     sum=sum+l[i]
# print(sum)


# Print sum of all elements in the list
# l=list(map(int,input().split()))
# sum=0
# for i in range(len(l)):
#     sum=sum+l[i]
# print(sum)


# Odd number element average in list
# l=list(map(int,input().split()))
# sum=c=0
# for i in range(len(l)):
#     if i%2==1:
#         sum=sum+l[i]
#         c=c+1
# print(sum/c)


# Even number element average in list
# l=list(map(int,input().split()))
# sum=c=0
# for i in range(len(l)):
#     if i%2==0:
#         sum=sum+l[i]
#         c=c+1
# print(sum/c)


# Print Prime Number in a present list
# l=list(map(int,input().split()))
# for i in l:
#     fc=0
#     for j in range(1,i+1):
#         if i%j==0:
#             fc=fc+1
#     if fc==2:
#         print(i)


# Print Next Prime number for every element in the list
# def p(a):
#     fc=0
#     for j in range(1,a+1):
#         if a%j==0:
#             fc=fc+1
#     return fc==2
# l=list(map(int,input().split()))
# for i in l:
#     ap=i+1
#     while(True):
#         if (p(ap)):
#             print(ap)
#             break
#         ap=ap+1


# Print List in reverse order
# l=list(map(int,input().split()))
# l.reverse()       # for i in range(len(l)-1,-1,-1):
# print(*l)              # print(l[i])



# Find sum of any two elements which is equal to key value
# l=list(map(int,input().split()))
# k=int(input())
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if (l[i]+l[j]==k):
#             print(l[i],l[j])


# Find index of an element in a list if it the element is repeated again it hsould also find the index value
# l=list(map(int,input().split()))
# n=int(input())
# if n in l:
#     k=0
#     c=l.count(n)
#     for i in range(c):
#         k=l.index(n,k)
#         print(k)
#         k=k+1
# else:
#     print("No Element Found")


# Remove element from the list which is repeated the same element again it should also remove 
# l=list(map(int,input().split()))
# n=int(input())
# if n in l:
#     c=l.count(n)
#     for i in range(c):
#         l.remove(n)
#     print(*l)
# else:
#     print("No Element Found")


# print sum of the elements up to given index in a list
# l=list(map(int,input().split()))
# i=int(input())
# if (i>=-(len(l)) and i<len(l)):
#     sum=0
#     if i>=0:
#         for j in range(i+1):
#             sum=sum+l[j]
#     else:
#         for j in range(-1,i-1,-1):
#             sum=sum+l[j]
#     print(sum)
# else:
#     print("No Element found")