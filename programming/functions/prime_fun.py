print("Check the Given Number is Prime or Not:")
def p(a):
    fc=0
    for i in range(1,a+1):
        if a%i==0:
            fc=fc+1
    return fc==2
n=int(input("Enter a number:"))
if (p(n)):
    print("Given Number is a Prime Number")
else:
    print("Given Number is Not a Prime Number")
print("The Prime Numebers from the Range are:")
def Range(x,y):
    c=0
    for i in range(x,y+1):
        if p(i):
            c=c+1
            if c==1:
                print(f"Prime Numbers from {x} to {y} are:",end=" ")
            if c>1:
                print(end=", ")
            print(i,end="")
    print()
x=int(input("Enter the First Integer:"))
y=int(input("Enter the Second Integer:"))
Range(x,y)
print("Find the Nearest Prime Number from the Given Number:")
def n_prime(p):
    t=int(input("Enter the Number:"))
    ap=t+1
    bp=t-1
    while(True):
        if p(ap):
            break
        ap=ap+1
    while(True):
        if p(bp):
            break
        bp=bp-1
    if (t-bp)<(ap-t):
        print(f"The Nearest Prime Number from {t} is:",bp)
    elif (ap-t)<(t-bp):
        print(f"The Nearest Prime Number from {t} is:",ap)
    else:
        print(f"The Nearest Prime Numbers from {t} are:",bp,ap)
n_prime(p)