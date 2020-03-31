a = input()
b = input()

x = int(a) * int(b[2])
y = int(a) * int(b[1])
z = int(a) * int(b[0])

sum = x + (y * 10) + (z * 100)

print(x, y, z, sum, sep = '\n')
