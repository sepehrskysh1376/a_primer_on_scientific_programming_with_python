from math import sqrt

def pathlength(x: list, y: list):
    """Computing the total length of a path"""
    n = len(x)
    L = 0
    for i in range(1, n):
        L += sqrt((x[i] - x[i-1])**2 + (y[i] - y[i-1])**2)
    return L

def test_pathlength():
    points = [[3, 4, 4], [4, 4, 6]]
    print("""
    An object going though these points (xi, yi):
    """)
    print(points[0])
    print(points[1])
    for i in range(len(points[0])):
        print(f"({points[0][i]}, {points[1][i]})")
    print("""
    The total path it would take is: %.3f
    And your function calculated:    %.3f
    And the error it has:            %.3f
          """ % (3., pathlength(points[0], points[1]), abs(3. - pathlength(points[0], points[1]))))


test_pathlength()
