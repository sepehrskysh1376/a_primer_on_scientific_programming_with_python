def hw1():
    return "Hello, World!"

def hw2():
    print("Hello, World!")

def hw3(*args):
    s = ""
    for i in args:
        s += i
    return s


print(hw1())
hw2()
print(hw3("Hello, ", "World!"))
print(hw3("Python ", "function"))
