n=int(input())
a=n*n
if a%10==n or a%100==n:
    print("automorphic number")
else:
    print("Not a automorphic number")