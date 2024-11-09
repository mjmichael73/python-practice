n1 = [1, 2, 3]
n2 = map(lambda x: x * x, n1)
n3 = filter(lambda x: x % 2 == 1, n1)
n4 =list(n2)
print(n1)
print(n2)
print(n3)
print(n4)