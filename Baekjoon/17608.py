n = int(input())

li = []
count = 0

for i in range(n) :
    a = int(input())
    li.append(a)

for i in range(len(li)-1) :
    if li[i] > li[-1] :
        count += 1

print(count + 1)