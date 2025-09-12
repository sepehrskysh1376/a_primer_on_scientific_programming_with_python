print("Generate an approximate Fahrenheit-Celsius conversion table\n\n")

f_temp_list = range(0, 101, 10)
c_temp_list = [round((f - 32) / (9/5), 1) for f in f_temp_list]
c_aprx_temp_list = [round((f - 30) / 2, 1) for f in f_temp_list]
conversion = [f_temp_list, c_temp_list, c_aprx_temp_list]

print("| Fahrenheit | Celsius | approximate Celsius |")

for i in range(0, len(conversion[0])):
    print(f"|------------|---------|---------------------|")
    
    f_temp = conversion[0][i]
    f_temp_str = str(i)
    f_temp_str_len = len(f_temp_str)

    c_temp = conversion[1][i]
    c_temp_str = str(c_temp)
    c_temp_str_len = len(c_temp_str)

    c_aprx_temp = conversion[2][i]
    c_aprx_temp_str = str(c_aprx_temp)
    c_aprx_temp_str_len = len(c_aprx_temp_str)


    print(f'|{(7 - f_temp_str_len)*" "}{i}     |{(6 - c_temp_str_len)*" "}{c_temp}   |{(12 - c_aprx_temp_str_len)*" "}{c_aprx_temp}         |')


