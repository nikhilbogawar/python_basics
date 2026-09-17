n=int(input())
dc=0
l=[]
t=n
while n>0:
    dc+=1
    r=n%10
    l.append(r)
    n=n//10
if dc<2:
    print("Invalid Input")
else:
    l.reverse()
    while True:
        s=0
        for i in l:
            s+=i
        if t!=s:
            l.remove(l[0])
            l.append(s)
            if s>t:
                print("Not a Keith Number")
                break
        else:
            print("Keith Number")
            break
#---------------------------------------------------------------
# n=int(input())
# dc=0
# l=[]
# t=n
# while n>0:
#     dc+=1
#     r=n%10
#     l.append(r)
#     n=n//10
# if dc<2:
#     print("iv")
# else:
#     l.reverse()
#     while True:
#         s=0
#         for i in l:
#             s+=i
#         if t!=s:
#             l.remove(l[0])
#             l.append(s)
#             if s>t:
#                 print("not a keith")
#                 break
#         else:
#             print("keith")
#             break