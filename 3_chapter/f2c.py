def f2c(f):
    """Function for Converting Fahrenheit to Celcius degrees"""
    return (5./9)*(f - 32)



def c2f(c):
    """Function for Converting Celcius to Fahrenheit degrees"""
    return (9./5)*c + 32


def f2c_test():
    c = 20
    if abs(f2c(c2f(c)) - c) < 1e-14:
        print("The test is succesful!")
    else:
        print("Failed the test")

f2c_test()

