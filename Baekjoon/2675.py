number = int(input())

for i in range(number) :
    li = list(map(str, input().split()))
    answer = ''
    for j in li[1] :
        for k in range(int(li[0])) :
            answer += j
    print(answer)
