print("Check the Given Number is Even or Odd:")
def m(a):
    return a%2==0
n=int(input("Enter a number:"))
if (m(n)):
    print("Given number is an Even number")
else:
    print("Given number is an Odd number")
print("The Even Numbers from the Range are:")
def Range(a,b):
    c=0
    for i in range(a,b+1):
        if m(i):
            c=c+1
            if c==1:
                print(f"Even Numbers from {a} to {b} are:",end=" ")
            if c>1:
                print(end=", ")
            print(i,end="")
    print()
a=int(input("Enter the First Integer:"))
b=int(input("Enter the Second Integer:"))
Range(a,b)
print("The Average of the Even Numebers from the Range are:")
def R_avg(p,q):
    c1=0
    sum=0
    for i in range(p,q+1):
        if m(i):
            c1=c1+1
            sum=sum+i
    print(f"The Average of Even Numbers from {p} to {q} is:",int(sum/c1))
p=int(input("Enter the First Integer:"))
q=int(input("Enter the Second Integer:"))
R_avg(p,q)