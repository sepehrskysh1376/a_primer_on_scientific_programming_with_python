from math import sqrt, cos, sin, pi

def pathlength(x: list, y: list):
    """Computing the total length of a path"""
    n = len(x)
    L = 0
    for i in range(1, n):
        L += sqrt((x[i] - x[i-1])**2 + (y[i] - y[i-1])**2)
    return L

def pi_approx(n):
    x = []
    y = []
    for i in range(0, n+1):
        x.append(cos(2.*pi*i/n)/2.)
        y.append(sin(2.*pi*i/n)/2.)
    return pathlength(x, y)

def test_pi_approx():
    k = range(2, 11)
    for i in k:
        n = 2**i
        print("with n = %4d => pi = %11.6f with error: %f%%" % (n, pi_approx(n), (abs(pi - pi_approx(n))/pi)*100))


test_pi_approx()


