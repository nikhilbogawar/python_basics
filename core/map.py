# a = [1, 2, 3, 4]
# b = [10, 20, 30, 40]
# k=list(map(lambda x,y:x+y,a,b))
# print(k)

# nums=[[1,2],[3,4],[5,6]]
# result=list(map(lambda x: x.append(10), nums))
# print("Result:", result)
# print("Nums:", nums)

# l=[[1,2],[3,4],[5,6]]
# k=list(map(lambda x:x+[5],l))
# print(k)

# s="Bogawar Nikhil"
# k=list(map(lambda x:ord(x),s))
# print(k)

# l=[5,10,15,20,25,30]
# k=list(map(lambda x:x**2,l))
# print(k)

# from functools import reduce
# k=[1,2,3,4,5,6,7,8,9,10]
# m=list(map(lambda x:x*7, filter(lambda x: x%3==0,k)))
# l=reduce(lambda x,y:x+y,m)
# print(l)     #126
#or
#Pipelines:---------------->>>
# from functools import reduce
# k=[1,2,3,4,5,6,7,8,9,10]
# m=reduce(lambda x,y:x+y, filter(lambda x:x%3==0, map(lambda x:x*7,k)))
# print(m)    #126

c = [23,22,26,10,15,20]
m = sorted(filter(lambda x: 60<x<120, map(lambda x: int(x*9/5)+32, c)), key=lambda x:x%4)
print(m)    #[68,73,78,71]

