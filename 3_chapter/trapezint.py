import math
from copy import copy

# a -----------------------------------------------------------
def trapezint1(f, a, b):
    """
    Trapezoidal rule for defined integration (Just one line)
    f: Integrating function
    a: The starting point
    b: The last point
    """
    assert b > a, "'b' should be bigger than 'a'."
    return ((b - a)/2)*(f(a) + f(b))

# b -----------------------------------------------------------

f1 = lambda x: math.cos(x)
f2 = lambda x: math.sin(x)

fun_str = ["cos(x)", "sin(x)", "sin(x)"]
trapezint_values = [trapezint1(f1, 0, math.pi), trapezint1(f2, 0, math.pi), trapezint1(f2, 0, math.pi/2.)]
exact_values = [0, 2, 1]

for i in range(0, len(fun_str)):
    print("Integrated function: %s with trapezint: %.3f and exact value: %.3f and the error: %.2e" % (fun_str[i], trapezint_values[i], exact_values[i], abs(trapezint_values[i] - exact_values[i])))


# c ------------------------------------------------------------
def trapezint2(f, a, b):
    """
    Trapezoidal rule for defined integration (Just two lines)
    f: Integrating function
    a: The starting point
    b: The last point
    """
    assert b > a, "'b' should be bigger than 'a'."
    sum = 0
    half_point = (b - a)/2
    sum += ((half_point - a)/2)*(f(a) + f(half_point))
    sum += ((b - half_point)/2)*(f(half_point) + f(b))

    return sum


fun_str = ["cos(x)", "sin(x)", "sin(x)"]
trapezint1_values = [trapezint1(f1, 0, math.pi), trapezint1(f2, 0, math.pi), trapezint1(f2, 0, math.pi/2.)]
trapezint2_values = [trapezint2(f1, 0, math.pi), trapezint2(f2, 0, math.pi), trapezint2(f2, 0, math.pi/2.)]
exact_values = [0, 2, 1]

for i in range(0, len(fun_str)):
    print("Integrated function: %s with 1line trapezint: %.3f with 2line trapezint: %.3f and exact value: %.3f and the 1line error: %.2e and the 2line error: %.2e" % (fun_str[i], trapezint1_values[i], trapezint2_values[i], exact_values[i], abs(trapezint1_values[i] - exact_values[i]), abs(trapezint2_values[i] - exact_values[i])))


# d -------------------------------------------------
def trapezint(f, a, b, n=10):
    """
    Trapezoidal rule for defined integration (With n lines)
    f: Integrating function
    a: The starting point
    b: The last point
    n: The number of trapezoid sides (integer)
    """
    h = (b - a)/float(n)
    points = [a]
    sum = 0
    for i in range(0, n):
        points.append(points[i]+h)
        sum += (h / 2.)*(f(points[i])+f(points[i+1]))
    return sum


print("----------------")
fun_str = ["cos(x)", "sin(x)", "sin(x)"]
a = [0, 0, 0]
b = [math.pi, math.pi, math.pi/2.]
trapezint1_values = [trapezint1(f1, a[0], b[0]), trapezint1(f2, a[1], b[1]), trapezint1(f2, a[2], b[2])]
trapezint2_values = [trapezint2(f1, a[0], b[0]), trapezint2(f2, a[1], b[1]), trapezint2(f2, a[2], b[2])]
n = 10
trapezint_values  = [trapezint(f1, a[0], b[0], n=n), trapezint(f2, a[1], b[1], n=n), trapezint(f2, a[2], b[2], n=n)]
exact_values = [0, 2, 1]


for i in range(0, len(fun_str)):
    print("""
    Integrated function: %s (From %1f to %1f)
     with 1line trapezint: %.3f,
     with 2line trapezint: %.3f,
     with %iline trapezint: %.3f
     and exact value: %.3f
     The 1line error: %.2e
     and the 2line error: %.2e
     and the %iline error: %.2e\n\n
    """ % (fun_str[i], a[i], b[i], trapezint1_values[i], trapezint2_values[i], n, trapezint_values[i], exact_values[i], abs(trapezint1_values[i] - exact_values[i]), abs(trapezint2_values[i] - exact_values[i]), n, abs(trapezint_values[i] - exact_values[i])))


# e ----------------------------------------------------------
def test_trapezint():
    ...


# extra ------------------------------------------------------
def eff_trapezint(f, a, b, n=10):
    """
    More efficient Trapezoidal algorithm for defined integration (With n lines)
    f: Integrating function
    a: The starting point
    b: The last point
    n: The number of trapezoid sides (integer)
    """
    h = (b - a)/float(n)
    points = [a]
    fac = (h/2.)*(f(a) + f(b))
    sum = 0
    for i in range(0, n):
        sum += f(points[i])
        points.append(points[i]+h)
    return fac + h*sum


print("----------------")
fun_str = ["cos(x)", "sin(x)", "sin(x)"]
a = [0, 0, 0]
b = [math.pi, math.pi, math.pi/2.]
trapezint1_values = [trapezint1(f1, a[0], b[0]), trapezint1(f2, a[1], b[1]), trapezint1(f2, a[2], b[2])]
trapezint2_values = [trapezint2(f1, a[0], b[0]), trapezint2(f2, a[1], b[1]), trapezint2(f2, a[2], b[2])]
n = 10
trapezint_values  = [trapezint(f1, a[0], b[0], n=n), trapezint(f2, a[1], b[1], n=n), trapezint(f2, a[2], b[2], n=n)]
eff_trapezint_values = [eff_trapezint(f1, a[0], b[0], n=n), eff_trapezint(f2, a[1], b[1], n=n), eff_trapezint(f2, a[2], b[2], n=n)]

exact_values = [0, 2, 1]


for i in range(0, len(fun_str)):
    print("""
    Integrated function: %s (From %1f to %1f)
     with 1line trapezint: %.3f,
     with 2line trapezint: %.3f,
     with %iline trapezint: %.3f,
     with %iline more efficient trapezint: %.3f
     and exact value: %.3f
     The 1line error: %.2e
     and the 2line error: %.2e
     and the %iline error: %.2e
     and the %iline error: %.2e\n\n
    """ % (fun_str[i], a[i], b[i], trapezint1_values[i], trapezint2_values[i], n, trapezint_values[i], n, eff_trapezint_values[i], exact_values[i], abs(trapezint1_values[i] - exact_values[i]), abs(trapezint2_values[i] - exact_values[i]), n, abs(trapezint_values[i] - exact_values[i]), n, abs(eff_trapezint_values[i] - exact_values[i])))

