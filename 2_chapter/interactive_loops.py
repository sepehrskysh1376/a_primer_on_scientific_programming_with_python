numbers = list(range(10))
print(numbers)
for n in numbers:
    i = int(len(numbers)/2)
    del numbers[i]
    print(f"n = {n}, del {i} of {numbers}")
