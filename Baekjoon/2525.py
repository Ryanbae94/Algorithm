hr, mn = map(int, input().split())
time = int(input())

if (mn + time) >= 60:
    hr =  (hr + (mn + time) // 60) % 24
    mn = (mn + time) % 60
else:
    mn += time

print(hr, mn)