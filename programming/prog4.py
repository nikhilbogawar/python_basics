# Print Pronic Numbers Up to a Given Limit
a = int(input())

for i in range(1, a + 1):
    if i % 2 == 0:
        b = (i * (i + 2)) // 4
        if b > a:
            break
        print(b,end=" ")    # 02 6 12 20 if the input is 25