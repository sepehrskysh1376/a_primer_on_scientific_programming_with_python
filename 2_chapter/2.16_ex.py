# The data from 2.7_ex.py
# a
v0 = 2
g = 9.8
n = 10
t_list = [(2*v0/g)*i for i in range(0, n+1)]
y_values = [v0 * t + 0.5 * g * t**2 for t in t_list]

ty1 = [t_list, y_values] # Nested list

space_num = 5*" "
print(f"|{space_num}t{space_num}|{space_num}y{space_num}|")
for row in range(0, len(t_list)):
    print(25*"-")
    t_str_len = len(str(round(ty1[0][row], 2)))
    y_str_len = len(str(round(ty1[1][row], 2)))
    print(f"|{(6-t_str_len)*" "}{round(ty1[0][row],2)}{5*" "}|{(7-y_str_len)*" "}{round(ty1[1][row],2)}{4*" "}|")
    

# b
print("\n\n")
ty2 = []
for i in range(0,len(t_list)):
    ty2.append([t_list[i], y_values[i]])

space_num = 5*" "
print(f"|{space_num}t{space_num}|{space_num}y{space_num}|")
for row in range(0, len(t_list)):
    print(25*"-")
    t_str_len = len(str(round(ty2[row][0], 2)))
    y_str_len = len(str(round(ty2[row][1], 2)))
    print(f"|{(6-t_str_len)*" "}{round(ty2[row][0],2)}{5*" "}|{(7-y_str_len)*" "}{round(ty2[row][1],2)}{4*" "}|")

