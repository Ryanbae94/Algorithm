n = int(input())

a= n // 2

for i in range(1, n+1) :
    if n % 2 == 1:
        print('* ' * (n - a))
        print(' *' * a)
    elif n % 2 == 0:
        print('* ' * a)
        print(' *' * (n - a))