cases = int(input())

def over_avr(list) :
    average = 0
    count = 0
    over_average = 0
    for i in range(1, len(list)) :
        average += list[i]
    average /= list[0]
    for i in range(1, len(list)) :
        if list[i] > average :
            count += 1
    
    over_average += float(count / list[0])
    over_average *= 100
    print("%0.3f%%"%over_average)

for i in range(cases) :
    li = list(map(int, input().split()))
    over_avr(li)

