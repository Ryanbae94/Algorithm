import time
start = time.time()

a, b = map(int, input().split())

min = min(a, b)
max = max(a, b)
sum = ((max - min) * (max - min + 1)) // 2

print(sum + (min *(max - min + 1)))
print(time.time() - start)
