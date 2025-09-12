eps = 1.0
c = 0 
while 1.0 != 1.0 + eps:
    print("..............", eps)
    eps = eps/2.0
    c += 1
print("final eps:", eps)
print(f"( 2^(1/{c} )")
