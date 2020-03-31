a, b = map(lambda x: int(x, 2), input().split())

sum = bin(a + b)

print(sum[2:])