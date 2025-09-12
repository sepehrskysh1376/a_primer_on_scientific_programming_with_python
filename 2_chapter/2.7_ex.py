# a
v0 = 2
g = 9.8
n = 10
t_list = [(2*v0/g)*i for i in range(0, n+1)]
y_values = [v0 * t + 0.5 * g * t**2 for t in t_list]

print ("|     t     |     y     |")
for row in range(0, len(y_values)):
    t = round(t_list[row], 2)
    y = round(y_values[row], 2)
    
    t_str = str(t)
    y_str = str(y)
    t_str_len = len(t_str)
    y_str_len = len(y_str)
    
    print ("-------------------------")
    print(f"|{(7-t_str_len)*" "}{t}    |{(7-y_str_len)*" "}{y}    |")

print("\n\n")
c = 0
print ("|     t     |     y     |")
while c < len(t_list):
    t = round(t_list[c], 2)
    y = round(y_values[c], 2)
    
    t_str = str(t)
    y_str = str(y)
    t_str_len = len(t_str)
    y_str_len = len(y_str)
    
    print ("-------------------------")
    print(f"|{(7-t_str_len)*" "}{t}    |{(7-y_str_len)*" "}{y}    |")
    c += 1
