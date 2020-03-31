import time
start = time.time()

hr, mn, sec = map(int, input().split())
t = int(input())

while t > 0 :
    sec += 1
    if sec == 60 :
        sec = 0
        mn += 1
        if mn == 60 :
            mn = 0
            hr += 1
            if hr == 24 :
                hr = 0
    t -= 1

print(hr, mn ,sec)
print(time.time() - start)