people_index = []
sum = 0

for i in range(4) :
    minus, plus = map(int, input().split())
    sum += plus
    sum -= minus
    people_index.append(sum)
    i += 1

print(max(people_index))