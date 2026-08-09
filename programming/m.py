# n=int(input())
# sq=n*n
# if str(sq).endswith(str(n)):
#     print("auto")
# else:
#     print("not auto")

a=int(input())
if a<=0:
    print("Invl")
else:
    s=str(a)
    s1=s+s
    b=True
    for i in range(len(s)):
        v=int(s1[i:i+len(s)])
        fc=0
        
        for j in range(1,v+1):
            if v%j==0:
                fc=fc+1
        if fc!=2:
            b=False
            break
    if b==True:
        print("C")
    else:
        print("not c")