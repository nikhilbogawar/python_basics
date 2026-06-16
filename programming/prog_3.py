a = float(input())
b = float(input())
c=0
while(round(a,1)<=b):
    c=c+1
    if c>1:
        print(end=", ")
    print(f"{a:.1f}^2",end="")
    a=a+0.2
print(".")




