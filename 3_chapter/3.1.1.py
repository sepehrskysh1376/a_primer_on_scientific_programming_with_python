def F(C):
    return (9.0/5) * C + 32

temp1 = F(15.5)
print(temp1)
a = 10
temp2 = F(a)
print(temp2)
print(F(a+1))
sum_temp = F(10) + F(20)
print(sum_temp)

# --------------------------------------------

Cdegrees = list(range(10, 50, 10))
Fdegrees = [F(C) for C in Cdegrees]
print(Cdegrees)
print(Fdegrees)

# --------------------------------------------

def F2(C):
    F_value = (9.0/5)*C + 32
    return f"{round(C, 1)} degrees Celsius corresponds to "\
           f"{round(F_value, 1)} degrees Fahrenheit"

s1 = F2(21)
print(s1)

# ---------------------------------------------

# c1 = 37.5
# s2 = F2(c1)
# print(F_value)

# ----------------------------------------------


