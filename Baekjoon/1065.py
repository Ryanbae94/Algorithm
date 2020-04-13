def hansu(number) :
    if number <= 99 :
        return True
    else :
        li = list(map(int, str(number)))
        if li[0] - li[1] == li[1] - li[2] :
            return True
        else :
            return False

n = int(input())
count = 0

for i in range(1, n+1) :
    if hansu(i) :
        count += 1

print(count)