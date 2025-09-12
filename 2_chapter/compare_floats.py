a = 1/947.0*947
b = 1
if a != b:
    print("Wrong result!")

tol = 1e-16
if abs(a - b) < tol:
    print("Second wrong result!")
