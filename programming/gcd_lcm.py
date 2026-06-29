#GCD or HCF
a=int(input())
b=int(input())
c=int(input())
if a<b and a<c:            # l=min(a,b,c)
    l=a
elif b<c:
    l=b
else:
    l=c
for i in range(l,0,-1):
    if a%i==0 and b%i==0 and c%i==0:
        print(i)
        break
    
#LCM
a=int(input())
b=int(input())
c=int(input())
h=max(a,b,c)
k=h
while(True):
    if h%a==0 and h%b==0 and h%c==0:
        print(h)
        break
    h=h+k