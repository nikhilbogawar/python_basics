# how many time the 'n' element in the list
# l=list(map(int,input().split()))
# n=int(input())
# c=0
# for i in range(len(l)):
#     if n==l[i]:
#         c=c+1
# print(l[i],"->",c)

# or we can write like this:--
# l=list(map(int,input().split()))
# for i in range(len(l)):
#     print(l[i],"->",l.count(l[i]))

# Backward Frequency:--->
# l=list(map(int,input().split()))
# for i in range(len(l)):
#     c=0
#     for j in range(i+1):
#         if l[i]==l[j]:
#             c=c+1
#     print(l[i],"->",c)

# frequency unique element:-->
# l=list(map(int,input().split()))
# for i in range(len(l)):
#     c=0
#     for j in range(len(l)):
#         if l[i]==l[j]:
#             c=c+1
#     if c==1:
#         print(l[i])

# frequency smallest element in unique element
# l=list(map(int,input().split()))
# s=float("inf")
# for i in range(len(l)):
#     c=0
#     for j in range(len(l)):
#         if l[i]==l[j]:
#             c=c+1
#     if c==1:
#         if l[j]<s:
#             s=l[i]
# print(s)

# backward frequency smallest unique element
# l=list(map(int,input().split()))
# s=float("inf")
# for i in range(len(l)):
#     c=0
#     for j in range(i+1):
#         if l[i]==l[j]:
#             c=c+1
#     if c==1:
#         if l[j]<s:
#             s=l[i]
# print(s)

# frequency count without repetition of elements
# l=list(map(int,input().split()))
# for i in range(len(l)):
#     c=0
#     for j in range(i):
#         if l[i]==l[j]:
#             c=c+1
#     if c==0:
#         print(l[i],"->",l.count(l[i]))
        
# frequency count without repetition of elements have duplicate count (means count more than 1)
# l=list(map(int,input().split()))
# for i in range(len(l)):
#     c=0
#     for j in range(i):
#         if l[i]==l[j]:
#             c=c+1
#     if (c==0) and (l.count(l[i])>1):
#         print(l[i],"->",l.count(l[i]))

# highest most repeated frequency and it should print that element
# l=list(map(int,input().split()))
# f=ele=0
# for i in range(len(l)):
#     c=0
#     for j in range(i):
#         if l[i]==l[j]:
#             c=c+1
#     if c==0:
#         c1=l.count(l[i])
#         if c1>f:
#             f=c1
#             ele=l[i]
# print(ele)