a = int(input())

for i in range(a) :
    li = list(str(input()))
    count = 0
    for j in li :
        if j == '(' :
            count += 1
        elif j == ')' :
            count -= 1
        if count < 0 :
            print("NO")
            break
    if count == 0 :
        print("YES")
    elif count > 0 :
        print("NO")