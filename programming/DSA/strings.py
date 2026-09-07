# given aadhar number is valid or not
a=input()
n=len(a)
if n==12 or n==14:
    if n==12:
        if a.isdigit():
            print("Valid")
        else:
            print("Invalid")
    else:
        l=a.split()
        if len(l)!=3:
            print("Invalid")
        else:
            for i in l:
                if not (len(i)==4 and i.isdigit()):
                    print("Invalid")
                    break
            else:
                print("Valid")
else:
    print("Invalid")
print("------------------------------------------------------------------")
# valid pancard or not
s=input()
if len(s)!=10:
    print("Invalid")
else:
    c=0
    for i in range(len(s)):
        if (i==0 or i==1 or i==2 or i==4 or i==9) and s[i]>='A' and s[i]<='Z':
            c+=1
        elif (i==8 or i==5 or i==6 or i==7) and s[i]>='0' and s[i]<='9':
            c+=1
        elif (i==3) and (s[i]=='P' or s[i]=='C' or s[i]=='F' or s[i]=='T' or s[i]=='A' or s[i]=='H'):
            c+=1
        else:
            print("Invalid")
            break
    if c==10:
        print("Valid")
print("------------------------------------------------------------------")
# password validation
p=input()
if len(p)<8:
    print("Invalid")
else:
    dc=cc=sc=spc=0
    for i in p:
        if i>='0' and i<='9':
            dc+=1
        elif i>='A' and i<='Z':
            cc+=1
        elif i>='a' and i<='z':
            sc+=1
        elif i!=' ':
            spc+=1
        else:
            print("Invalid")
            break
    if dc>0 and sc>0 and cc>0 and spc>0:
        print("Valid")
    else:
        print("Invalid")
print("------------------------------------------------------------------")
# searching in strings
# program to check a given substring exists
str=input()
inp=input()
for i in range(len(str)-len(inp)):
    w=str[i:i+len(inp)]
    if inp==w:
        print("Found")
        break
else:
    print("Not Found")
print("------------------------------------------------------------------")
# case conversions
# write a program to count number of uppercase and lowercase letters in a string
n=input()
l=c=0
for i in range(len(n)):
    if n[i]>='a' and n[i]<='z':
        l+=1
    elif n[i]>='A' and n[i]<='Z':
        c+=1
print(c,l)
print("------------------------------------------------------------------")
# program to separate alphabets, digits and special characters from a string
sep=input()
al=dig=sp=[]
for i in sep:
    if i.isalpha():
        al.append(i)
    elif i.isdigit():
        dig.append(i)
    else:
        sp.append(i)
print("".join(al))
print("".join(dig))
print("".join(sp))
print("-------------------------------------------------------------------")
# reversed of a string
r=input()
rev=[]
for i in range(len(r)-1,-1,-1):
    rev.append(r[i])
print("".join(rev))
print("-------------------------------------------------------------------")
# string frequency
# print frequency of each character in a string
of=input()
for i in range(len(of)):
    oc=0
    for j in range(len(of)):
        if of[i]==of[j]:
            oc+=1
    print(of[i],"->",oc)
print("-------------------------------------------------------------------")
# forward frequency
ff=input()
for i in range(len(ff)):
    fc=0
    for j in range(i):
        if ff[i]==ff[j]:
            fc+=1
    if fc==0:
        occ=0
        for j in range(len(ff)):
            if ff[i]==ff[j]:
                occ+=1
        print(ff[i],"->",occ)
print("------------------------------------------------------------------")
# backward frequency
bf=input()
for i in range(len(bf)-1,-1,-1):
    bc=0
    for j in range(i+1,len(bf)):
        if bf[i]==bf[j]:
            bc+=1
    if bc==0:
        ocb=0
        for j in range(len(bf)):
            if bf[i]==bf[j]:
                ocb+=1
        print(bf[i],"->",ocb)
print("------------------------------------------------------------------")
# most repeated character
mr=input()
mrcc=0
mrc=""
for i in range(len(mr)):
    mroc=0
    for j in range(len(mr)):
        if mr[i]==mr[j]:
            mroc+=1
    if mroc>mrcc:
        mrcc=mroc
        mrc=mr[i]
print(mrc)
print("-----------------------------------------------------------------")
# 2nd most repeated character
mr=input()
mrcc=0
mrc=""
smrcc=0
smrc=""
for i in range(len(mr)):
    mroc=0
    for j in range(len(mr)):
        if mr[i]==mr[j]:
            mroc+=1
    if mroc>mrcc:
        if mr[i]!=mrc:
            smrcc=mrcc
            smrc=mrc
        mrcc=mroc
        mrc=mr[i]
    elif mroc>smrcc and mr[i]!=mrc:
        smrcc=mroc
        smrc=mr[i]
print(smrc)