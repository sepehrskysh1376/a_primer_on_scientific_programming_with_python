
def H(x):
    """The Heaviside function"""
    if x < 0:
        return 0
    elif x >= 0:
        return 1

def I(x, L, R):
    """Indicator function, if in L and R range = 1, otherwise = 0"""
    return H(x - L)*H(R - x)

def piecewise(x, data):
    """
    A piecewise function connecting each range to a constant value
    x: The value we are looking for
    data: a list of pairs (vi, xi) for i = 0, ..., n
    """
    for i in range(len(data)-1):
        if data[i][1] <= x < data[i+1][1]:
            return data[i][0]
    if data[-1][1] <= x:
        return data[-1][0]
    return False

def piecewise2(x, data):
    """
    A piecewise function connecting each range to a constant value, with the help of Indicator function and the Heaviside function
    x: The value we are looking for
    data: a list of pairs (vi, xi) for i = 0, ..., n
    """
    sum = 0
    for i in range(len(data)-1):
        sum += data[i][0] * I(x, data[i][1], data[i+1][1])
    if data[-1][1] <= x:
        return data[-1][0]
    return sum


def test_piecewise():
    x = [1, 13, 142, 4921, 29987, 987987]
    data = [(1, 0), (2, 10), (3, 100), (4, 1000), ("<= 5", 10000)]
    for i in range(len(x)):
        print(f"What is the number of digits for %6d: {piecewise2(x[i], data)} and it is {piecewise(x[i], data) == piecewise2(x[i], data)}" % (x[i]))

test_piecewise()
