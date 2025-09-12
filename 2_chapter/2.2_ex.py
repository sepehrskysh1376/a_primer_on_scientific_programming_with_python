print("Generate an approximate Fahrenheit-Celsius conversion table\n\n")

f_temp_list = range(0, 101, 10)

print("| Fahrenheit | Celsius | approximate Celsius |")
for i in f_temp_list:
    print(f"|------------|---------|---------------------|")

    f_temp_str = str(i)
    f_temp_str_len = len(f_temp_str)

    c_temp = round((i - 32) / (9/5), 1)
    c_temp_str = str(c_temp)
    c_temp_str_len = len(c_temp_str)

    c_aprx_temp = round((i - 30) / 2, 1)
    c_aprx_temp_str = str(c_aprx_temp)
    c_aprx_temp_str_len = len(c_aprx_temp_str)


    print(f'|{(7 - f_temp_str_len)*" "}{i}     |{(6 - c_temp_str_len)*" "}{c_temp}   |{(12 - c_aprx_temp_str_len)*" "}{c_aprx_temp}         |')

