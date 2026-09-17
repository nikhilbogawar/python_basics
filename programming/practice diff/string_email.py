s=input()
f=s.find("@")
a=s.find(".",f)
c=0
if len(s)>=15 and len(s)<=25:
    for i in range(0,f):
        if i==f-1 and (s[i]=="." or s[i]=='_'):
            break
        if s[0].isalpha():
            if s[i].isalnum() or s[i]=='.' or s[i]=="_":
                c+=1
    for i in range(f+1,a):
        if s[i].isalnum():
            c+=1
    for i in range(a+1,len(s)):
        if s[i].isalpha():
            c+=1
    if c+2==len(s) and s[0].isalpha():
        print("Valid")
    else:
        print("Invalid")
else:
    print("Invalid")