h, m = map(int, input().split())

hour = h
minute = m - 45
if minute < 0:
    minute = 15 + m
    hour -= 1

if hour < 0:
    hour += 24

print(hour, minute)
