from math import sqrt

def SoE(N):
    """
    The Sieve of Eratosthenes algorithm for finding the prime numbers
    """
    if N <= 1:
        raise ValueError("The 'N' parameter cannot be equal or less than 1.")

    A = [True for i in range(2, N)]
    num1 = 2
    while num1 <= sqrt(N):
        if A[num1-2] == True:
            j = num1*num1
            print(A)
            while j < N:
                print(j)
                A[j-2] = False
                j += num1 
                print(A)
        num1 += 1
    num = 2
    for i in range(len(A)):
        if A[i] == True:
            print(num, end=" ")
        num += 1


SoE(30)
