def self_number(n) :
    for i in range(n) :
        num = 0
        origin = i
        while i != 0 :            
            num += i % 10
            i //= 10
        if origin + num == n :
            return False
            break
    return True

self_number_list = []

for i in range(1, 101):
    if self_number(i) :
        self_number_list.append(i)

for answer in self_number_list :
    print(answer)

