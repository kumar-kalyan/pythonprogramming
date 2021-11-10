def isSpecial(n):
    s = 0
    p = 1
    while(n > 0):
        r = n % 10
        s += r
        p *= r
        n //= 10
    if(s == p):
        return True
    else:
        return False

n = int(input("Enter a number"))

val = isSpecial(n)
if(val):
    print(n,' is a special number')
else:
    print(n,' is not a special number')
           
