from math import exp, pi, log, cos, sin

def diff(f, x, h=1E-5):
    "Numberical differentiation"
    return (f(x+h) - f(x-h)) / (2.*h)

# Differentiation of: a*x**2 + b*x + c
f1 = lambda x, a=2, b=3, c=4 : a*x**2 + b*x + c

f1_diffed = lambda x, a=2, b=3 : 2*a*x + b


def test_diff():
    a = 2
    b = 3
    c = 4
    x = 10.5
    
    exact = f1_diffed(x)
    numerical = diff(f1, x)
    print(f"The diff function exact:        {exact}")
    print(f"The diff function numerical:    {numerical} ")
    print(f"The error:                      {abs(exact - numerical)}")


f2 = lambda x : exp(x)
f2_diffed = lambda x : exp(x)
f3 = lambda x : exp(-2 * x**2)
f3_diffed = lambda x : -4*x*exp(-2 * x**2)
f4 = lambda x : cos(x)
f4_diffed = lambda x : -sin(x)
f5 = lambda x : log(x)
f5_diffed = lambda x : 1/x

def test_diff2():
    h = 0.01
    x = 0
    exact = f2_diffed(x)
    numerical = diff(f2, x, h)
    print("f(x) = exp(x)")
    print(f"The diff function exact:        {exact}")
    print(f"The diff function numerical:    {numerical} ")
    print(f"The error:                      {abs(exact - numerical)}")
    print("----------------------------")
    x = 0
    exact = f3_diffed(x)
    numerical = diff(f3, x, h)
    print("f(x) = exp(-2*x**2)")
    print(f"The diff function exact:        {exact}")
    print(f"The diff function numerical:    {numerical} ")
    print(f"The error:                      {abs(exact - numerical)}")
    print("----------------------------")
    x = 2*pi
    exact = f4_diffed(x)
    numerical = diff(f4, x, h)
    print("f(x) = cos(x)")
    print(f"The diff function exact:        {exact}")
    print(f"The diff function numerical:    {numerical} ")
    print(f"The error:                      {abs(exact - numerical)}")
    print("----------------------------")
    x = 1
    exact = f5_diffed(x)
    numerical = diff(f5, x, h)
    print("f(x) = ln(x)")
    print(f"The diff function exact:        {exact}")
    print(f"The diff function numerical:    {numerical} ")
    print(f"The error:                      {abs(exact - numerical)}")
    print("----------------------------")





test_diff()
test_diff2()
