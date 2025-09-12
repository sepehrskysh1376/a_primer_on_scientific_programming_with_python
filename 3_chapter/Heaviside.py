def H(x):
    """The Heaviside function"""
    if x < 0:
        return 0
    elif x >= 0:
        return 1

def test_H():
    x_list = [-10, -1e-15, 0, 1e-15, 10]
    x_types = ['d', '.e', 'd', '.e', 'd']
    print("Testing H() function for value: x = %d, %.e, %d, %.e, %d" % tuple(x_list))
    for i in range(len(x_list)):
        print(f"H(%{x_types[i]}) is correct: %d" % (x_list[i], H(x_list[i])))

test_H()
