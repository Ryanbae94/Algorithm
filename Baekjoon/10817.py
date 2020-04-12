li = list(map(int, input().split()))
a = max(li)
b = min(li)

li.remove(a)
li.remove(b)

print(li[0])