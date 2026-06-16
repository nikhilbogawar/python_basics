# l=["Hello","elephant","Lion","lesson","Owl"]
# k=list(filter(lambda x: bool(x) and x[0].isupper(),l))
# m=list(filter(lambda y: bool(y) and y[0].islower(),l))
# print(k)       # ['Hello', 'Lion', 'Owl']
# print(m)       # ['elephant', 'lesson']

# chain map() and filter to the list upto 1 to 10 filter out odds and print the remaining evens and for every even element square it
# l=[1,2,3,4,5,6,7,8,9,10]
# k=list(filter(lambda x:x%2==0 ,l))
# print(k)
# m=list(map(lambda x:x**2 ,k))
# print(m)

# nums=[12,15,7,18,20,21,25]
# k=list(filter(lambda x:(x%3==0) ^ (x%5==0),nums))
# print(k)

# d={"apple": 100, "Banana": 40, "cherry": 150}
# k=list(filter(lambda x:d[x]>50,d))
# m=list(filter(lambda x:x>50,d.values()))
# print(k)      # ['apple', 'cherry']
# print(m)      # [100, 150]

# s="Bogawar Nikhil"
# k=list(filter(lambda x: x not in "AEIOUaeiou",s))
# print(''.join(k))  # Bgwr Nkhl

