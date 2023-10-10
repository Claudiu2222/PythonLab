matrix_of_characters = [
    ["f", "i", "r", "s"],
    ["n", "_", "l", "t"],
    ["o", "b", "a", "_"],
    ["h", "t", "y", "p"],
]


def print_matrix_in_spiral_order(matrix):
    final_string = ""
    matrix_length = len(matrix)
    for current_level in range(0, matrix_length // 2):
        for top_row in range(current_level, matrix_length - current_level):
            final_string += matrix[current_level][top_row]
        for right_column in range(current_level + 1, matrix_length - current_level):
            final_string += matrix[right_column][matrix_length - current_level - 1]
        for bottom_row in range(matrix_length - current_level - 1, current_level, -1):
            final_string += matrix[matrix_length - current_level - 1][bottom_row - 1]
        for left_column in range(
            matrix_length - current_level - 1, current_level + 1, -1
        ):
            final_string += matrix[left_column - 1][current_level]
    if matrix_length % 2 == 1:
        final_string += matrix[matrix_length // 2][matrix_length // 2]
    return final_string


print(print_matrix_in_spiral_order(matrix_of_characters))
