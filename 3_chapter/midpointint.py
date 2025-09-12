import math

def midpoint(f, a, b, n=10):
    """
    Computation of Definite Integrals with Midpoint rule
    f: pre-integral function
    a: starting point
    b: end point
    n: number of rectangles
    """
    h = (b - a)/n
    #heights = [h/2.]
    sum = 0
    for i in range(0, n):
        sum += f(a + i*h + (h * (1./2.)))
    return h*sum

def trapezint(f, a, b, n=10): # Example of 'trapezint.py' file
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


f1 = lambda x: math.cos(x)
f2 = lambda x: math.sin(x)

print("----------------")
fun_str = ["cos(x)", "sin(x)", "sin(x)"]
a = [0, 0, 0]
b = [math.pi, math.pi, math.pi/2.]
n = 10
midpoint_values  = [midpoint(f1, a[0], b[0], n=n), midpoint(f2, a[1], b[1], n=n), midpoint(f2, a[2], b[2], n=n)]
trapezint_values  = [trapezint(f1, a[0], b[0], n=n), trapezint(f2, a[1], b[1], n=n), trapezint(f2, a[2], b[2], n=n)]

exact_values = [0, 2, 1]


for i in range(0, len(fun_str)):
    print("""
    Integrated function: %s (From %1f to %1f)
     with %iline Trapezint: %.3f,
     with %iline Midpoint: %.3f
     and exact value: %.3f
     and the %iline Trapezint error: %.2e
     and the %iline Midpoint error: %.2e\n\n
    """ % (fun_str[i], a[i], b[i], n, trapezint_values[i], n, midpoint_values[i], exact_values[i], n, abs(trapezint_values[i] - exact_values[i]), n, abs(midpoint_values[i] - exact_values[i])))


