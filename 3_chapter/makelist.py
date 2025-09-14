

def makelist(start, stop, inc):
    value = start
    result = []
    while value <= stop:
        result.append(value)
        value += inc
        print(result)
    return result

#print(makelist(0, 100, 1))
#print(makelist(0, 100, 0.1))
#print(makelist(-1, 1, 0.1))
#print(makelist(10, 20, 20))
#print(makelist([1, 2], [3, 4], [5]))
#print(makelist((1, -1, 1), ("myfile.dat", "yourfile.dat")))
print(makelist("myfile.dat", "yourfile.dat", "herfile.dat"))
