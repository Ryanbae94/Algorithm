alphabet_string = 'abcdefghijklmnopqrstuvwxyz'
alphabet_number = []
for i in range(26) :
    alphabet_number.append(-1)

li = input()

for i in range(len(li)) :
    for j in range(len(alphabet_string)) :
        if li[i] == alphabet_string[j] and alphabet_number[j] == -1 :
            alphabet_number[j] = i

ans = ''

for i in alphabet_number :
    ans += str(i) + ' '

print(ans)

