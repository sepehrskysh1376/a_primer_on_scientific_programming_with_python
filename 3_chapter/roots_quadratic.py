def roots(a, b, c):
    """Finding the roots for quadratic equations: ax^2 + bx + c = 0"""
    from numpy.lib.scimath import sqrt
    delta = (b*b) - 4*a*c
    x1 = (-b + sqrt(delta))/(2*a)
    x2 = (-b - sqrt(delta))/(2*a)
    return x1, x2

def test_roots_float():
    x1, x2 = roots(2, -3, -5)
    print("The calculated roots are: %.2f and %.2f" % (x1, x2))
    assert (abs(2.5 - x1) < 1e-14 and abs(-1. - x2) < 1e-14), "The 'roots' function is not working!" 

def test_roots_complex():
    from numpy.lib.scimath import sqrt
    x1, x2 = roots(2, -3, 5)
    print("The calculated roots are: %.2f+%.2fi and %.2f+%.2fi" % (x1.real, x1.imag, x2.real, x2.imag))
    assert (abs((3./4) - x1.real) < 1e-14) and (abs(sqrt(31./16) - x1.imag) < 1e-14) and (abs((3./4) - x2.real) < 1e-14)  and (abs(-sqrt(31./16) - x2.imag) < 1e-14) , "The 'roots' function is not working!" 



test_roots_float()
test_roots_complex()


