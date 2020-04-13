def self_number(i) :
    for j in range(i) :
        num = 0
        origin = j
        while j != 0 :            
            num += j % 10
            j //= 10
        if origin + num == i :
            return False
            break
    return True

print(self_number(42))

