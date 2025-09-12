import math

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

def double_derivative(f, x, h):
    return (f(x+h) - 2*f(x) + f(x-h))/float(h*h)

def adaptive_trapezint(f, a, b, eps=1E-5, numx = 5000):
    """Adapte in respect to its eps (Error) estimation to first guess the n and then calculate the numerical integral with Trapezint rule"""
    f_second_abs_list = []
    small_value = (b-a)/float(numx)
    for i in range(1, numx):
        f_second_abs_list.append(abs(double_derivative(f, a+(i*small_value), small_value)))

    h = math.sqrt(12*eps)*((b-a)*max(f_second_abs_list))**(-1/2)
    n = int((b-a)/float(h))
    points = [a]
    sum = 0
    for i in range(0, n):
        points.append(points[i]+h)
        sum += (h / 2.)*(f(points[i])+f(points[i+1]))
    return sum, n


f1 = lambda x: math.cos(x)
f2 = lambda x: math.sin(x)


print("----------------")
fun_str = ["cos(x)", "sin(x)", "sin(x)"]
a = [0, 0, 0]
b = [math.pi, math.pi, math.pi/2.]
ada_trapezint_values  = [adaptive_trapezint(f1, a[0], b[0]), adaptive_trapezint(f2, a[1], b[1]), adaptive_trapezint(f2, a[2], b[2])]
exact_values = [0, 2, 1]


for i in range(0, len(fun_str)):
    print("""
    Integrated function: %s (From %1f to %1f)
     with adaptive trapezint: %.3f with %iline
     and exact value: %.3f
     and the %iline error: %.2e\n\n
    """ % (fun_str[i], a[i], b[i], ada_trapezint_values[i][0], ada_trapezint_values[i][1], exact_values[i], ada_trapezint_values[i][1], abs(ada_trapezint_values[i][0] - exact_values[i])))
    





