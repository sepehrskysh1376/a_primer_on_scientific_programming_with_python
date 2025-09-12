def a(x):
    print("inside a q:%i" % q)
    print("inside a x:%i" % x)
    q = 2
    x = 3*x
    return q + x

def b(x):
    print("inside b q:%i" % q)
    print("inside b x:%i" % x)
    global q
    q += x
    return q + x

q = 0
x = 3

print("outside q:%i" % q)
print("outside x:%i" % x)
print(a(x))
print("outside q:%i" % q)
print("outside x:%i" % x)
print(b(x)) 
print("outside q:%i" % q)
print("outside x:%i" % x)
print(a(q))
print("outside q:%i" % q)
print("outside x:%i" % x)
print(b(q))
