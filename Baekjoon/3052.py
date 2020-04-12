# li = []

# for i in range(10) :
#     a = int(input())
#     li.append(a % 42)

# li = set(li)

# print(len(li))


li = []
temp = []

for i in range(10) :
    a = int(input())
    li.append(a % 42)

for i in li :
    if i in temp :
        pass
    else :
        temp.append(i)

print(len(temp))