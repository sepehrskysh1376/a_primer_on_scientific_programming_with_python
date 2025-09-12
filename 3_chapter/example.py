import math

def Simpson(f, a, b, n=500):
    """
    Numerical integration with Simpson's rule approximation of function f.

    f: The function
    a: The starting value (float)
    b: The last value (float)
    n: The iteration number for accuracy (integer)

    Example:
    >>>
    >>>
    """
    h = (b - a)/float(n)

    fac = (b - a)/(3*n)
    fa = f(a)
    fb = f(b)

    halfn = round(n/2)
    
    sum1 = 0
    for i in range(1, halfn+1):
        sum1 += f(a + (2*i - 1)*h)

    sum2 = 0
    for i in range(1, halfn):
        sum2 += f(a + 2*i*h)

    return fac * (fa + fb + 4*sum1 + 2*sum2)



f1 = lambda x, a=-2, b=5: a*x + b 
f2 = lambda x, a=-20, b=10, c=30: a*(x*x) + b*(x) + c
f3 = lambda x: (3./float(2))*math.sin(x)**3
f1_exactInt = lambda x, a=5:  -x**2 + 5*x
f2_exactInt = lambda x, a=-20, b=10: (-20/3)*(x**3) + 5*x**2 + 30*x
f3_exactInt = lambda x: (3./2)*( ((math.cos(x)**3)/3) - math.cos(x) )

# -----------------------
fun = [f1, f2, f3]
fun_exactInt = [f1_exactInt, f2_exactInt, f3_exactInt]
a = 0
b = math.pi
for i in range(0, 3):
    approx_int = Simpson(fun[i], a, b)
    exact_int = fun_exactInt[i](b)-fun_exactInt[i](a)
    error = abs(approx_int - exact_int)
    print("Approx. Integral value: %.2f, Exact Integral value: %.2f, error: %.1e" % (approx_int, exact_int, error))


def application():
    print("Integral of 1.5*sin^3 from 0 to pi")
    for n in [2, 6, 12, 100, 500]:
        approx = Simpson(f3, 0, math.pi, n)
        print("n=%3d, approx=%18.15f, error=%9.2E" % (n, approx, 2-approx))

application()
