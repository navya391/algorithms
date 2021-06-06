n = int(input())
num = [0, 1]
if n <= 0:
    print(n)
else:
    for i in range(2, n+1):
        num3 = num[i-1] + num[i-2]
        num.append(num3)
    print(num[-1])
