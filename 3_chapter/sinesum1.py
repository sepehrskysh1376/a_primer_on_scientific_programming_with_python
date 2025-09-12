from math import sin, pi

def S(t, n, T):
    """
    The approximation for f(t)
    """
    sum = 0
    for i in range(1, n):
        sum += (1/(2*i - 1))*sin((2*(2*i - 1)*pi*t)/T)
    return (4/pi)*sum


def f(t, T):
    """
    The piecewise constant function
    """
    if 0. < t < T/2.:
        return 1
    elif abs(t - T/2.) < 1e-7:
        return 0
    elif T/2. < t < T:
        return -1

def table():
    n = [1, 3, 5, 10, 30, 100]
    alpha = [0.01, 0.25, 0.49]
    T = 2 * pi
    print("  n    t    error")
    
    for j in alpha:
        for i in n:
            print("%3d %.4f %.4f" %(i, j*T, abs(f(j*T, T)-S(j*T, i, T))))

table()

