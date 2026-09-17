l=list(map(int,input().split()))
n=int(input())
if n>0:
    b=True
    for i in range(len(l)):
        c=0
        for j in range(i+1,len(l)):
            if l[i]+l[j]==n:
                print(l[i],l[j])
                c+=1
                b=False
    if b==True:
        print("No Pairs Found")
else:
    print("Invalid Key Value")