def poly(x, roots):
    """
    Computing polynomial function from its roots
    p(x) = ax^n + bx^(n-1) + ... + wx^2 + yx + z = 0
    """
    mul = 1
    for root in roots:
        mul *= (x - root)
    return mul

def test_poly():
    test_roots = [1, 5, -3]
    x = 8
    answer = 231
    print("the poly function: %f, The answer: %f" % (poly(x, test_roots), answer))
    assert abs(poly(x, test_roots) - answer) < 1E-14, "The 'poly' function is not working properly."
    print("Succeed!")

test_poly()
