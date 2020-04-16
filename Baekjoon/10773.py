a = int(input())
li = []
count = 0
for i in range(a) :
    num = int(input())
    if num != 0 :
        li.append(num)        
    else :
        li.pop()

print(sum(li))
