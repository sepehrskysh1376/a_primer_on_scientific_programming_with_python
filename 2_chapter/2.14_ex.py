a = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h']]
print(a[0][0])
print(a[1])
print(a[-1][-1])
print(a[1][0])
print(a[-1][-2])

for i in range(0, len(a)):
    for j in range(0, len(a[i])):
        print(a[i][j])
