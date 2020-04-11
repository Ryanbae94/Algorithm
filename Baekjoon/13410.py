n, m = map(int, input().split())
li = []
reverse_li = []

for i in range (1, m+1) :
    li.append(n * i)

for i in li :
    reverse_li.append(int(str(i)[::-1]))

print(max(reverse_li))