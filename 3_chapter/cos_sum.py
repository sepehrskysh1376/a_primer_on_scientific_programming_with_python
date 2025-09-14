from math import pi, cos

def C(x, n = 100):
    """
    Cosine function approximation as a series of summation with certain relationship between the each summation term
    x: The independent variable (cos(x))
    n: The number of summation, increasing the accuracy
    """
    x = float(x)
    term = 1
    s = term
    for i in range(1, n+1):
        term = -term*((x*x) / (2*i*(2*i - 1)))
        s += term
    return s


def test_table_C():
    x = [(4*pi + i*2*pi) for i in range(4)]
    n = [5, 25, 50, 100, 200]
    
    print("%3s" % ("x"), end="")
    for j in n:
        print("%13d" % (j), end="")
    print()
    for i in x:
        print("%-9.4f" % (i), end="")
        for j in n:
            print("%12.2e" % (abs(C(i, j)-cos(i))), end="")
        print()


test_table_C()

