n = 9

if n % 2 == 0:
    n -= 1

c = 0
while c != n+1:
    if c % 2 != 0:
        print(c)
    c += 1
