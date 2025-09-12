
def H(x):
    """The Heaviside function"""
    if x < 0:
        return 0
    elif x >= 0:
        return 1


def if_x_in_range(x, L, R):
    """Testing if x is in the range of L and R, bool return"""
    if L <= x <= R:
        return True
    else:
        return False

def I(x, L, R):
    """Indicator function, if in L and R range = 1, otherwise = 0"""
    return H(x - L)*H(R - x)

def test_I():
    L = 5; R = 10
    x = [L-1e-15, L, (L+R)/2., R, R+1e-15]
    x_types = ['e', 'd', 'f', 'd', 'e']
    print(f"Using indicator for checking if the following values are between {L}-{R}:")
    print("x = %e, %d, %f, %d, %e" % tuple(x))
    for i in range(len(x)):
        print(f"I(%{x_types[i]}; {L}, {R}) = %d (inside or not: {if_x_in_range(x[i], L, R)})" % (x[i], I(x[i], L, R)))

test_I()
