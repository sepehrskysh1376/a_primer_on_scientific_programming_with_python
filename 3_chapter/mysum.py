def mysum(lis):
    """
    Adding any type of elements together.
    First defnining the type and then sum them together.
    """
    if type(lis[0]) in [float, int, complex]:
        s = 0
        for number in lis:
            s += number
    elif type(lis[0]) == str:
        s = ''
        for string in lis:
            s += string
    else:
        s = []
        for element in lis:
            s += element
    return s


def mysum2(lis):
    """
    Adding any type of elements together.
    More general on type usage
    * Except, 'set' and 'dictionary' type.
    """
    first_element = lis[0]
    for i in range(1, len(lis)):
        first_element += lis[i]
    return first_element

print(mysum([1, 3, 5, -5]))
print(mysum([[1, 2], [4, 3], [8, 1]]))
print(mysum(['Hello, ', 'World!']))

print(mysum2([1, 3, 5, -5]))
print(mysum2([[1, 2], [4, 3], [8, 1]]))
print(mysum2(['Hello, ', 'World!']))
print(mysum2((1, 2, 3, 4)))

        
