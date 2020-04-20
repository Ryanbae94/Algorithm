def gcd_r(a, b):
    if b == 0 :
        return a
    else :
        return gcd_r(b, a%b)

print(gcd_r(10, 20))