li = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

word = list(input())
ans = 0
# 1 is considered to be primenumber in this algorithm case
def isPrime(num) :
    if num != 1 :
        for i in range(2, num) :
            if num % i == 0 :
                return False
            else :
                return True
    else :
        return True

for i in word :
    for j in range(len(li)) :
        if i == li[j]:
            ans += j + 1

if isPrime(ans) :
    print("It is a prime word.")
else :
    print("It is not a prime word.")

print(ans, isPrime(ans))
