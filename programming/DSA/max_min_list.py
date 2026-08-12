# nth highest and smallest number in a list without using predefined function
# l=list(map(int,input().split()))
# h=float("-inf")
# for i in range(len(l)):
#     if l[i]>h:
#         h=l[i]
# print(h)
# s=float("inf")
# for i in range(len(l)):
#     if l[i]<s:
#         s=l[i]
# print(s)

l=list(map(int,input().split()))
h1=float("-inf")
h2=h1
for i in range(len(l)):
    if l[i]>h1:
        h2=h1
        h1=l[i]
    elif l[i]>h2:
        h2=l[i]
print(h1,h2)