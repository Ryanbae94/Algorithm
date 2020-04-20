import sys
input = sys.stdin.readline

def isPrime(num) :
    a = [False, False] + [True] * (num-1)
    for i in range(2, (len(a) // 2) + 1) :
        if a[i] :
            for j in range(i + i, num, i) :
                a[j] = False
    return a  

primes = isPrime(1000000)
                                       
while True :
    n = int(input().strip())

    if n == 0 :
        break
    else :
        for i in range(n // 2) :
            if primes[i] and primes[n - i] :
                print("%d = %d + %d" %(n, i, n-i))
                break
