a = int(input())

def sugar(number) :
    for three_box in range((number // 3) + 1) :
        for five_box in range((number // 5) + 1) :
            if ((three_box * 3 + five_box * 5) == number) :
                return (three_box + five_box)
    return -1

print(sugar(a))

def sugar1(number) :

    three_box = 0
    five_box = number // 5
    number %= 5

    while five_box >= 0 :
        if number % 3 == 0 :
            three_box = number // 3
            number %= 3
            break
        five_box -= 1
        number += 5
    
    print(number == 0 and (three_box + five_box) or -1)

sugar1(a)