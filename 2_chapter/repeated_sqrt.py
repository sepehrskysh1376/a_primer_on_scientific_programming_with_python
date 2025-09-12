from math import sqrt
for n in range(1, 60):
    r = 2.0
    for i in range(n):
        r = sqrt(r)
    for i in range(n):
        r = r**2
    print(f"{n} times sqrt and **2: {round(r, 16)}")


# Investigation:
n = 52
r = 2.0
for i in range(n):
    r = sqrt(r)
    print(f"sqrt(r) {i}th time = {r}")
for i in range(n):
    r = r**2
    print(f"r**2 {i}th time = {r}")


for n in range(1, 60):
    r = 2.0
    for i in range(n):
        r = sqrt(r)
        r = r**2
    print(f"{n} times sqrt and **2: {round(r, 16)}")

