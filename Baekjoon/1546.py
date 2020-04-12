import copy
n = int(input())

li = list(map(int, input().split()))
li2 = copy.deepcopy(li)

for i in range(n) :
    li[i] = float(li[i] / max(li2)) * 100

print(float(sum(li)/n)) 