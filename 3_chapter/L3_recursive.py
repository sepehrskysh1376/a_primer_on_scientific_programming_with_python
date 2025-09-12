
def L3(x, epsilon = 1.0e-6):
    x = float(x)
    i = 1
    term = (1.0/i) * (x/(1+x))**i
    s = term
    while abs(term) > epsilon:
        i += 1
        term = (1.0/i)*(x/(1+x))**i
        s += term
    return s, i

def L3_ci(x, epsilon = 1.0e-6):
    """Natural lograithm for x+1 (ln(x+1) = this function)"""
    x = float(x)
    i = 1
    term = (1.0/i) * (x/(1+x))**i
    s = term
    while abs(term) > epsilon:
        i += 1
        term *= (x/(1+x))*((i-1)/(i))
        s += term
    return s, i


def test_L3_ci():
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    epsilon = 1.0e-6
    for i in range(len(x)):
        print(f"For x = {x[i]}:")
        print("The L3 is    : %f with %d tries reached %e precision" % (L3(x[i])[0], L3(x[i])[1], epsilon))
        print("The L3_ci is : %f with %d tries reached %e precision" % (L3_ci(x[i])[0], L3_ci(x[i])[1], epsilon))
        print("The error is : %f" % (abs(L3(x[i])[0] - L3_ci(x[i])[0])))
        print("----------------")


test_L3_ci()

