number = int(input())

for i in range(number) :
    string = str(input())
    score = 0
    count = 0
    for j in range(len(string)) :
        if string[j] == 'O' :
            count += 1
            score += count
        elif string[j] == 'X' :
            score += 0
            count = 0
    print(score)
