# list questions using dictionary method:---->>>>>

# count the number of unique elements
# l=list(map(int,input().split()))
# d={}
# res=[]
# for i in range(len(l)):
#     c=0
#     for j in range(len(l)):
#         if l[i]==l[j]:
#             c+=1
#     if c==1:
#         res.append(l[i])
# if len(res)>0:
#     d=len(res)
# else:
#     d="No Unique Elements"
# print(d)

# all rotations anti-clockwise
# l=list(map(int,input().split()))
# d={}
# rotations=[]
# for i in range(len(l)):
#     new_list=[]
#     for j in range(len(l)):
#         new_list.append(l[(i+j)%len(l)])
#     rotations.append(new_list)
# d=rotations
# for r in rotations:
#     print(*r)

# least unique element
# l=list(map(int,input().split()))
# d={}
# least=float("inf")
# for i in range(len(l)):
#     c=0
#     for j in range(len(l)):
#         if l[i]==l[j]:
#             c+=1
#     if c==1 and l[i]<least:
#         least=l[i]
# d=least
# if least==float("inf"):
#     print("No Uniques in the Array")
# else:
#     print(least)

# all possible sublists
# l=list(map(int,input().split()))
# d={}
# sublists=[]
# for i in range(len(l)):
#     for j in range(i,len(l)):
#         sub=[]
#         for k in range(i,j+1):
#             sub.append(l[k])
#         sublists.append(sub)
# d=sublists
# for s in sublists:
#     print(*s)

# sub-arrays with sum equal to key
# l=list(map(int,input().split()))
# n=int(input())
# d={}
# subarrays=[]
# for i in range(len(l)):
#     for j in range(i,len(l)):
#         s=0
#         sub=[]
#         for k in range(i,j+1):
#             s+=l[k]
#             sub.append(l[k])
#         if s==n:
#             subarrays.append(sub)
# s=subarrays
# if len(subarrays)>0:
#     for ss in subarrays:
#         print(*ss)
# else:
#     print("No Sub Arrays Found")

# all rotations clockwise
# l=list(map(int,input().split()))
# d={}
# rotations=[]
# for i in range(len(l)):
#     new_list=[]
#     for j in range(len(l)):
#         new_list.append(l[(j-i)%len(l)])
#     rotations.append(new_list)
# d=rotations
# for r in rotations:
#     print(*r)

# count duplicates
# l=list(map(int,input().split()))
# d={}
# dc=0
# c=0
# for i in range(len(l)):
#     for j in range(len(l)):
#         if l[i]==l[j]:
#             c+=1
#     if c>1:
#         bc=0
#         for k in range(0,i+1):
#             if l[i]==l[k]:
#                 bc+=1
#         if bc==1:
#             dc+=1
#     c=0
# d=dc
# if dc==0:
#     print("No Duplicates Found")
# else:
#     print(dc)