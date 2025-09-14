
data = [# name          distance to sun  apprent BN     Luminosity
        ("Alpha Centaruri A",       4.3,    0.26,       1.56),
        ("Alpha Centaruri B",       4.3,    0.077,      0.45),
        ("Alpha Centaruri C",       4.2,    0.00001,    0.00006),
        ("Barnard's Star",          6.0,    0.00004,    0.00005),
        ("Wolf 359",                7.7,    0.000001,   0.0005),
        ("BD +36 degrees 2147",     8.2,    0.0003,     0.006),
        ("Luyten 726-8 A",          8.4,    0.000003,   0.00006),
        ("Luyten 726-8 B",          8.4,    0.000002,   0.00004),
        ("Sirius A",                8.6,    1.00,       23.6),
        ("Sirius B",                8.6,    0.001,      0.003),
        ("Ross 154",                9.4,    0.00002,    0.0005)
]

def mysort(i, a):
    """
    Getting an index value "i" for list "a":
    return a value (negative or positive integer) that if sorted, 
    """
    ...

def table(data, sorting_info):
    """
    It is a sorting table function, printing each star's name and the sorted_info in front of it in a sorted manner. 
    data: Your data
    sorting_info:   choosing which information you want to be sorted (by their index)
                    1: Distance in respect to sun
                    2: Apparent brightness
                    3: Luminosity
    """
    name_list = [data[i][0] for i in range(len(data))]
    prop_list = [data[i][sorting_info] for i in range(len(data))]
    sorted_name_list = []
    sorted_prop_list = []
    for i in range(len(data)):
        m = max(prop_list)
        max_index = prop_list.index(m)
        sorted_name_list.append(name_list[max_index])
        sorted_prop_list.append(m)
        name_list.pop(max_index)
        prop_list.pop(max_index)
    
    for i in range(len(sorted_name_list)):
        print("%-20s %.2e" % (sorted_name_list[i], sorted_prop_list[i]))


table(data, 3)
