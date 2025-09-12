from math import factorial

def fact(n):
    """Getting the Factorial of number n"""
    if n == 1 or n == 0:
        return 1

    return n*fact(n-1)

n = 5 
print(f"The factorial of {n} is: {fact(n)}")
