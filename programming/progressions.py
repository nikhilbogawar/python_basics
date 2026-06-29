# Arithmetic Progression------------------------------
# AP Series
a=int(input())
d=int(input())
n=int(input())
for i in range(n):
    print((a+i*d),end=" ")
# AP Sum
a=int(input())
d=int(input())
n=int(input())
sum=0
for i in range(n):
    ap=a+i*d
    sum=sum+ap
print(sum)
# AP only Nth value
a=int(input())
d=int(input())
n=int(input())
print(a+(n-1)*d)

# Geometric Progression---------------------------------
# GP Series
a=int(input())
r=int(input())
n=int(input())
for i in range(n):
    print((a*(r**i)),end=" ")
# GP Sum
a=int(input())
r=int(input())
n=int(input())
sum=0
for i in range(n):
    gp=a*(r**i)
    sum=sum+gp
print(sum)
# GP only Nth value
a=int(input())
r=int(input())
n=int(input())
print(a*(r**i))

# Harmonic Progression----------------------------------
# HP Series
a=int(input())
d=int(input())
n=int(input())
for i in range(n):
    hp=1/(a+i*d)
    print("%.2f"%(hp),end=" ")
# HP Sum
a=int(input())
d=int(input())
n=int(input())
sum=0
for i in range(n):
    hp=1/(a+i*d)
    sum=sum+hp
print("%.2f"%(sum))
#HP only Nth value
a=int(input())
d=int(input())
n=int(input())
hp=1/(a+(n-1)*d)
print("%.2f"%(hp))