a = int(input())
li = list(map(int, input().split()))
ans = 0
li.sort()

for i in range(1, len(li)) :
    ans += (li[i] - li[i - 1]) * i * (a - i)

print(ans * 2)