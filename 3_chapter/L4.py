

def L4(x, n = None, epsilon = None, return_n = True):
    """
    The Logarithm approximation for x+1 (= ln(x+1) )
    """
    x = float(x)
    if n is not None:
        s = 0
        for i in range(1, n+1):
            s += (1.0/i)*(x/(1+x))**i
        if return_n == True:
            return s, i
        else:
            return s

    elif epsilon is not None:
        i = 1
        term = (1.0/i) * (x/(1+x))**i
        s = term
        while abs(term) > epsilon:
            i += 1
            term = (1.0/i)*(x/(1+x))**i
            s += term
        if return_n == True:
            return s, i
        else:
            return s
    else:
        raise ValueError("Both of 'n' and 'epsilon' parameters cannot get 'None' argument.")

print(L4(4, epsilon = 1e-12))
