# print even numbers in a nested list
r=int(input("Enter the row input: "))
nl=[]
for n in range(0,r):
    nl.append(list(map(int,input().split())))
print("even numbers in nested list:---->>")
def even_numbers(nl):
    for i in range(0,len(nl)):
        for j in range(0,len(nl[i])):
            if nl[i][j]%2==0:
                print((nl[i][j]))
even_numbers(nl)
#---------------------------------------------------------------------
# print all the prime numbers in a nested list
print("prime numbers in nested list:---->>")
def prime_numbers(nl):
    for i in range(0,len(nl)):
        for j in range(0,len(nl[i])):
            p=nl[i][j]
            fc=0
            for k in range(1,p+1):
                if p%k==0:
                    fc+=1
            if fc==2:
                print(p)
prime_numbers(nl)
#---------------------------------------------------------------------
# print sum of all elements in a nested list
print("Sum of elements in nested list:---->>")
def sum_elements(nl):
    sum=0
    for i in range(0,len(nl)):
        for j in range(0,len(nl[i])):
            sum+=nl[i][j]
    print(sum)
sum_elements(nl)
#---------------------------------------------------------------------
# search an element in a nested list
print("search an element in nested list:---->>")
search=int(input("Enter the number to search in nested list: "))
def search_ele(nl,search):
    for i in range(0,len(nl)):
        for j in range(0,len(nl[i])):
            if nl[i][j]==search:
                print("found")
                return
    print("not found")
search_ele(nl,search)
#---------------------------------------------------------------------
print("maximum number in a nested list:---->>")
def max_num(nl):
    max=float("-inf")
    for i in range(0,len(nl)):
        for j in range(0,len(nl[i])):
            if nl[i][j]>max:
                max=nl[i][j]
    print(max)
max_num(nl)
#--------------------------------------------------------------------
print("Second highest number in a nested list:---->>")
def sec_max_num(nl):
    h1=h2=float("-inf")
    for i in range(0,len(nl)):
        for j in range(0,len(nl[i])):
            val=nl[i][j]
            if val>h1:
                h2=h1
                h1=val
            elif val>h2 and val!=h1:
                h2=val
    print(h2)
sec_max_num(nl)
#--------------------------------------------------------------------
print("Sum of inner list of a nested list:---->>")
def inner_sum(nl):
    for i in range(0,len(nl)):
        sum=0
        for j in range(0,len(nl[i])):
            sum+=nl[i][j]
        print(sum)
inner_sum(nl)
#--------------------------------------------------------------------
print("Maximum of the diagonal elements:---->>")
def max_ele_diagonal(nl):
    dia_max=float("-inf")
    for i in range(0,len(nl)):
        if nl[i][i]>dia_max:
            dia_max=nl[i][i]
    print(dia_max)
max_ele_diagonal(nl)
#--------------------------------------------------------------------
print("sum of both diagonal elements separately:---->>")
def sum_dia_both(nl):
    sump=sums=0
    for i in range(0,len(nl)):
        sump+=nl[i][i]
        sums+=nl[i][len(nl)-1-i]
    print(sump,sums)
sum_dia_both(nl)
#---------------------------------------------------------------------
print("Identity matrix or not:---->>")
def identity(nl):
    for i in range(0,len(nl)):
        if len(nl)!=len(nl[i]):
            print("not an identity matrix")
            return
        for j in range(0,len(nl[i])):
            if i==j and nl[i][j]!=1:
                print("not an identity matrix")
                return
            elif i!=j and nl[i][j]!=0:
                print("not an identity matrix")
                return
    print("identity matrix")
identity(nl)
#----------------------------------------------------------------------
print("traverse the matrix elements in columnwise:---->>")
def traverse_column(nl):
    for i in range(0,len(nl[0])):
        for j in range(0,len(nl)):
            print(nl[j][i],end=" ")
        print()
traverse_column(nl)
#----------------------------------------------------------------------