a = int(input())
li = []

for i in range(a) :
    num = int(input())
    li.append(num)

li.sort()

for i in range(len(li)) :
    print(li[i])
