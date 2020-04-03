x = int(input())
y = int(input())

def quadrant(number_x, number_y) :
    if number_x > 0 and number_y > 0 :
        print("1")
    elif number_x < 0 and number_y > 0 :
        print("2")
    elif number_x < 0 and number_y < 0 :
        print("3")
    else :
        print("4")

quadrant(x, y)
