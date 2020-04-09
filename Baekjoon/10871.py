n, x = map(int, input().split())
li = list(map(int, input().split()))
ans = []

for i in li :
    if i < x :
        ans.append(i)

for j in range(len(ans)) :
    print(ans[j], end=' ')