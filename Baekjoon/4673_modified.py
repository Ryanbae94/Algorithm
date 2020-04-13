def self_number(n) :
    result = n    
    while n != 0 :
        result += n % 10
        n //= 10
    return result

not_self_number_list = []
self_number_list = []

for i in list(range(1, 10001)) :
    not_self_number_list.append(self_number(i))
    if i not in not_self_number_list :
        self_number_list.append(i)

for i in self_number_list :
    print(i)