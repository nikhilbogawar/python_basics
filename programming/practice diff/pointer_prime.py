n=int(input())
if n<=0:
    print("Invalid Input.")
else:
    s=str(n)
    pro=1
    for i in s:
        pro=pro*int(i)
    ns=n+pro
    np=n+1
    while True:
        fc=0
        for i in range(1,np+1):
            if np%i==0:
                fc+=1
        if fc==2:
            c=np
            break
        np=np+1
    if c==ns:
        print(f"{n} is a Pointer Prime Number")
    else:
        print(f"{n} is Not a Pointer Prime Number")
# -----------------------------------------------------------------
# n=int(input())
# if n<=0:
#     print("iv")
# else:
#     s=str(n)
#     pro=1
#     for i in s:
#         pro=pro*int(i)
#     ns=n+pro
#     np=n+1
#     while True:
#         fc=0
#         for i in range(1,np+1):
#             if np%i==0:
#                 fc+=1
#         if fc==2:
#             c=np
#             break
#         np+=1
#     if c==ns:
#         print("is a pointer")
#     else:
#         print("not a pointer")
# ------------------------------------------------------------------------
# not this one:--->>>
# n=int(input())
# if n<=0:
#     print("Invalid Input")
# else:
#     s=str(n)
#     pro=1
#     for i in s:
#         pro=pro*int(i)
#     ns=n+pro
#     for i in range(1,ns+1):
#         fc=0
#         for j in range(1,i+1):
#             if i%j==0:
#                 fc+=1
#     if fc==2:
#         print("pointer")
#     else:
#         print("not pointer")