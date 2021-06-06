n = int(input())
nums = input()
x = nums.split(" ")
s = []
for i in x:
    number = int(i)
    s.append(number)
m1 = max(s)
s.remove(m1)
m2 = max(s)
s.remove(m2)
product = m1*m2
print(product)






