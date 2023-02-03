initial_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


# My solution
# def rotate_matrix_90(matrix):
#     rotated_matrix = [
#
#     ]
#
#     for row_index in range(len(matrix) - 1, -1, -1):
#         rotated_row = []
#         for col_index in range(len(matrix[0]) - 1, -1, -1):
#             rotated_row.append(matrix[col_index][row_index])
#         rotated_matrix.append(rotated_row)
#
#     rotated_matrix.reverse()
#     return rotated_matrix


def rotate_matrix_90(matrix):
    n = len(matrix)

    for layer in range(n // 2):
        first = layer
        last = n - layer - 1
        for i in range(first, last):
            # Save top element
            top = matrix[layer][i]
            # move left element to top
            matrix[layer][i] = matrix[-i - 1][layer]
            # move bottom element to top
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]
            # move right to bottom
            matrix[-layer - 1][-i - 1] = matrix[i][-layer - 1]
            # move top to right
            matrix[i][-layer - 1] = top
    return matrix


print(rotate_matrix_90(initial_matrix))
