def greatest_div(num1, num2):
    if num2 == 0:
        print(num1)
    else:
        while num2 != 0:
            num3 = (num1 % num2)
            num1 = num2
            num2 = num3
        if num2 == 0:
            print(num1)


a, b = map(int, input().split(" "))
greatest_div(a, b)