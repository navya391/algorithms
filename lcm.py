def lcm_num(num1, num2):
    m = num1
    n = num2
    if n == 0:
        print(m)
    else:
        while n != 0:
            num3 = (m % n)
            m = n
            n = num3
        if n == 0:
            x = (num2 // m)
            y = (num1 // m)
            result = (x * y * m)
            print(result)


a, b = map(int, input().split(" "))
lcm_num(a, b)
