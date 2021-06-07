i = int(input())
if i < 5:
    print(i)
elif 5 <= i < 10:
    n = i % 5
    print(n+1)
else:
    g = i//10
    m = i % 10
    if m != 0 and 5 <= m < 10:
        n = m % 5
        print(g+n+1)
    elif m != 0 and m < 5:
        print(g+m)
    else:
        print(g)
