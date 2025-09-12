# a
a = 10
b = 20
n = 5
space = (b-a) / n
x_coord = []

x = a
for i in range(0, n+1):
    x_coord.append(x)
    x += space
print(x_coord)

# b

x_coord = [a+(space*i) for i in range(0, n+1)]
print(x_coord)
