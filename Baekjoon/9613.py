import itertools

def gcd(a, b):
    if b == 0 :
        return a
    else :
        return gcd(b, a%b)

n = int(input())

for i in range(n) :
    li = list(map(int, input().split()))
    li = li[1:]        
    ans = 0
    for a, b in itertools.combinations(li, 2) :
        ans += gcd(a, b)
    print(ans)
    