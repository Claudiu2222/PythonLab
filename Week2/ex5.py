def replace_elements_under_main_diagonal(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if i > j:
                matrix[i][j] = 0


matrix = [
    [1, 2, 3, 4, 5],
    [4, 5, 6, 7, 3],
    [2, 1, 9, 6, 4],
    [2, 4, 2, 1, 2],
    [2, 4, 2, 1, 25],
]
replace_elements_under_main_diagonal(matrix)
print(matrix)
