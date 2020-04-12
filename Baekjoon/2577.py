a = int(input())
b = int(input())
c = int(input())

count = 0
li = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

sum = str(a * b * c)

for i in sum:
    li[int(i)] += 1

for i in range(len(li)):
    print(li[i], end = "\n")
