def gauss(x, m=0, s=1):
    """Gaussian function"""
    from math import exp, sqrt, pi
    return (1/(sqrt(2*pi)*s))*exp(-((x - m)/s)**2/2.)

def table(n = 100, m = 0, s = 1):

    space = 10*s / float(n)

    print("     x          f(x)")
    print("---------------------------")

    for i in range(0, n+1):
        x = m - 5*s + i*space
        print("%10.3f %10.3f" %(x, gauss(x)))


table()

