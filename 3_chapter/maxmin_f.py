from math import cos, pi

def maxmin(f, a, b, n=1000):
    """Finding the maximum and minimum of a function from the value a to b"""
    f_values = []
    h = (b-a)/(n-1)
    for i in range(n):
        f_values.append(f(a + i*h))
    return min(f_values), max(f_values)

def test_maxmin():

    f = lambda x : cos(x)
    a = -pi/2.
    b = 2.*pi
    print("The maximum value is: %9f" % (maxmin(f, a, b)[0]))
    print("The minimum value is: %9f" % (maxmin(f, a, b)[1]))

test_maxmin()
