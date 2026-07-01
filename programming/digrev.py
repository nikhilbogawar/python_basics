n = int(input())
t = n
dc = 0
while t > 0:
    dc = dc + 1
    t = t // 10
t = n
for i in range(dc):
    last = n % 10            
    rest = n // 10           
    k = last * (10**(dc-1)) + rest
    print(k)
    n = k
    if n == t:            
        break
