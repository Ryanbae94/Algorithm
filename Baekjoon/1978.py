n = int(input())
li = list(map(int, input().split()))
ans = 0

def isPrimeNum(num) :
    if num < 2 :
        return False
    for i in range(2, num) :
        if num % i == 0 :
            return False
    return True

for i in li :
    if isPrimeNum(i) :
        ans += 1

print(ans)