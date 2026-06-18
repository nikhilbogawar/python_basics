# check weather the given number is a perfect square or not
n=int(input())
b=False
for i in range(1,n+1):
    if i*i==n:
        b=True
        break
    if i*8>n:
        break
if b==True:
    print("The Given Number is a Perfect Square")
else:
    print("The Given Number is not a Perfect Square")