# Basic Sorthing
# l=list(map(int,input().split()))
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]>l[j]:
#             l[i],l[j]=l[j],l[i]
# print(*l)

# nth largest element in a list
# l=list(map(int,input().split()))
# n=int(input())
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]>l[j]:
#             l[i],l[j]=l[j],l[i]
# print(l[len(l)-n])

# first four smallest missing elements in a list
# l=list(map(int,input().split()))
# s=min(l)+1
# c=0
# while(True):
#     if s not in l:
#         print(s)
#         c=c+1
#         if c==4:
#             break
#     s=s+1

# is element in the list or not
# l=list(map(int,input().split()))
# n=int(input())
# b=False
# for i in range(len(l)):
#     if n==l[i]:
#         b=True
#         break
# if b==True:
#     print('Found')
# else:
#     print('Not Found')

# finding element in a list
l=list(map(int,input().split()))
n=int(input())
l.sort()
s,e=0,len(l)-1
b=False
while s<=e:
    m=(s+e)//2
    if l[m]==n:
        b=True
        break
    elif n>l[m]:
        s=m+1
    else:
        e=m-1
if b==True:
    print("Found")
else:
    print("Not Found")