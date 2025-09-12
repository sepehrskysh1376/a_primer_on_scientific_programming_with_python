from math import cos, pi

def my_max(a):
    """Finding the maximum value from a list"""
    max_elem =a[0]
    for i in range(1, len(a)):
        if max_elem < a[i]:
            max_elem = a[i]
    return max_elem

def my_min(a):
    """Finding the maximum value from a list"""
    min_elem =a[0]
    for i in range(1, len(a)):
        if min_elem > a[i]:
            min_elem = a[i]
    return min_elem

def maxmin(f, a, b, n=1000):
    """Finding the maximum and minimum of a function from the value a to b"""
    f_values = []
    h = (b-a)/(n-1)
    for i in range(n):
        f_values.append(f(a + i*h))
    return min(f_values), max(f_values)

def my_maxmin(f, a, b, n=1000):
    f_values = []
    h = (b-a)/(n-1)
    for i in range(n):
        f_values.append(f(a + i*h))
    return my_min(f_values), my_max(f_values)


def test_maxmin():

    f = lambda x : cos(x)
    a = -pi/2.
    b = 2.*pi
    print("The maximum value is: %9f" % (maxmin(f, a, b)[0]))
    print("The minimum value is: %9f" % (maxmin(f, a, b)[1]))
    print("My maximum value is : %9f" % (my_maxmin(f, a, b)[0]))
    print("My minimum value is : %9f" % (my_maxmin(f, a, b)[1]))

test_maxmin()
