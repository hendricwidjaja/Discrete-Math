def add_matrix(m1,m2):
    try:
        m1[0][0]
        is_2D = True
    except TypeError:
        is_2D = False

    if not is_2D:
        if len(m1) != len(m2):
            return None
        matrix_add = []
        for i in range(len(m1)):
            result = m1[i] + m2[i]
            matrix_add.append(result)
        return matrix_add

    for i in range(len(m1)):
        if len(m1[i]) != len(m2[i]):
            return None
    
    matrix_add = []

    for i in range(len(m1)):
        result_row = []

        for j in range(len(m1[i])):
            result = m1[i][j] + m2[i][j]
            result_row.append(result)
        matrix_add.append(result_row)

    return matrix_add
    
m1 = [[1],[1],[1]]
m2 = [[1],[1],[1]]
m3 = [1,1,1]
m4 = [1,1,1]

print 

result = add_matrix(m3, m4)
print(result)

# def add_matrix(m1,m2):
#     if len(m1) == len(m2):

#         matrix_add = []

#         for i in range(len(m1)):
#             result_row = []

#             for j in range(len(m1[i])):
#                 result = m1[i][j] + m2[i][j]
#                 result_row.append(result)
#             matrix_add.append(result_row)

#         return matrix_add
    
#     else:
#         return None
    
# m1 = [[1],[1],[1]]
# m2 = [[1],[1],[1]]

# result = add_matrix(m1, m2)
# print(result)