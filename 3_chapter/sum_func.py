def sum_1k(M):
    """Summation of 1/k"""
    sum = 0
    for k in range(1, M+1):
        sum += 1/float(k)
    return sum


def test_sum_1k():
    s1k = sum_1k(3)
    exact_s = 11/6
    assert abs(s1k - exact_s) < 1E-14, "The summation function and the value are not close to each other."
    print("Success!")


test_sum_1k()
