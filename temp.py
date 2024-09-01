def add_matrix(m1,m2):
    if len(m1) == len(m2):

        matrix_add = []

        for i in range(len(m1)):
            result_row = []

            for j in range(len(m1[i])):
                result = m1[i][j] + m2[i][j]
                result_row.append(result)
            matrix_add.append(result_row)

        return matrix_add
    
    else:
        return None
    
m1 = [[1],[1],[1]]
m2 = [[1],[1],[1]]

result = add_matrix(m1, m2)
print(result)