def get_list_of_people_who_cannot_see(matrix):
    seats_of_people_who_cannot_see = []
    columns = len(matrix[0])
    rows = len(matrix)

    for i in range(0, columns):
        max_column_height = -1
        for j in range(0, rows):
            if matrix[j][i] > max_column_height:
                max_column_height = matrix[j][i]
            else:
                seats_of_people_who_cannot_see.append((j, i))
    return seats_of_people_who_cannot_see


matrix = [
    [1, 2, 3, 2, 1, 1],
    [2, 4, 4, 3, 7, 2],
    [5, 5, 2, 5, 6, 4],
    [6, 6, 7, 6, 7, 5],
]
print(get_list_of_people_who_cannot_see(matrix))
