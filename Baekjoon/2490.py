tmp = list(map(int, input().split()))
tmp1 = list(map(int, input().split()))
tmp2 = list(map(int, input().split()))

def yut(list) :
    x = 0
    y = 0
    
    for i in list :
        if i == 0 :
            x += 1
        else :
            y += 1

    if x == 1 and y == 3 :
        print('A')
    elif x == 2 and y == 2 :
        print('B')
    elif x == 3 and y == 1 :
        print('C')
    elif x == 4 and y == 0 :
        print('D')
    else : 
        print('E')

yut(tmp)
yut(tmp1)
yut(tmp2)

    