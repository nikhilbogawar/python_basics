# a=int(input())
# b=int(input())
# if a>b:
#     c=0
#     for i in range(a,b-1,-1):
#         c=c+1
#         if c>1:
#             print(end=",")
#         print(f"{i}@{i-1}",end="")
# else:
#     c=0
#     for i in range(a,b+1):
#         c=c+1
#         if c>1:
#             print(end=",")
#         print(f"{i}@{i+1}",end="")
# output : 10@9,9@8,8@7,7@6,6@5,5@4,4@3,3@2,2@1,1@0,0@-1,-1@-2,-2@-3,-3@-4,-4@-5,-5@-6


# a=int(input())
# b=int(input())
# if a>b:
#     c=0
#     for i in range(a,b-1,-1):
#         c=c+1
#         if c>1:
#             print(end=", ")
#         if i<0:
#             print(f"5*({i})",end="")
#         else:
#             print(f"5*{i}",end="")
# else:
#     c=0
#     for i in range(a,b+1):
#         c=c+1
#         if c>1:
#             print(end=", ")
#         if i<0:
#             print(f"5*({i})",end="")
#         else:
#             print(f"5*{i}",end="")
# output : 5*8, 5*7, 5*6, 5*5, 5*4, 5*3, 5*2, 5*1, 5*0, 5*(-1), 5*(-2), 5*(-3), 5*(-4), 5*(-5), 5*(-6), 5*(-7)

# a=int(input())
# b=int(input())
# if a>b:
#     c=0
#     for i in range(a,b-1,-1):
#         c=c+1
#         if c>1:
#             print(end=", ")
#         if i<0:
#             print(f"({i*5})",end="")
#         else:
#             print(f"{i*5}",end="")
# else:
#     c=0
#     for i in range(a,b+1):
#         c=c+1
#         if c>1:
#             print(end=", ")
#         if i<0:
#             print(f"({i*5})",end="")
#         else:
#             print(f"{i*5}",end="")
# output : 50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 0, (-5), (-10), (-15), (-20), (-25), (-30), (-35)

# a=float(input())
# b=float(input())
# c=0
# while(round(a,1)<=b):
#     c=c+1
#     if c>1:
#         print(end=", ")
#     print(f"{a:.1f}^2",end="")
#     a=a+0.2
# print(".")
# output : 5.0^2, 5.2^2, 5.4^2, 5.6^2, 5.8^2, 6.0^2, 6.2^2, 6.4^2, 6.6^2, 6.8^2, 7.0^2.

# a=int(input())
# if a==0:
#     print("Zero")
# a=abs(a)

# c=0
# for i in range(1,a+1):
#     c=c+1
#     if c>1:
#         print(end=", ")
    
#     if i%3==1:
#         print("1",end="")
#     elif i%3==0:
#         print("@",end="")
#     else:
#         print("A",end="")
# output : 1, A, @, 1, A, @, 1, A, @, 1