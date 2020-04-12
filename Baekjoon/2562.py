li = []
for i in range(9) :
    a = int(input())
    li.append(a)

print(max(li), li.index(max(li)) + 1)