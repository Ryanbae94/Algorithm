number = int(input())
origin_num = number
new_num = 0
temp = 0
count = 0

while True :
    temp = (number % 10 + number // 10) % 10
    new_num = (number % 10) * 10 + temp
    count += 1
    number = new_num
    if new_num == origin_num :
        break

print(count)