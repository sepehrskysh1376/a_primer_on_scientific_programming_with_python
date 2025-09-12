def area(vertices: list):
    """
    Using a set of three point creating a triangle to compute area of it
    """
    sum = 0.
    indeces = list(range(len(vertices)))
    for i in indeces:
        x_index = i+1
        y_index_pos = x_index + 1
        y_index_neg = x_index - 1
        if y_index_pos > len(vertices): # check for not going outside the bound
            y_index_pos -= 3
        if y_index_neg < 1:
            y_index_neg += 3
        sum += vertices[x_index-1][0]*vertices[y_index_pos-1][1] - vertices[x_index-1][0]*vertices[y_index_neg-1][1]
    return abs(sum)/2


triangle1 = area([[1, 0], [0, 2], [0, 0]])
print("Area of triangle is %.2f" % triangle1)





