# Chapter 1 problem 8
def zero_matrix(matrix):
    cols = len(matrix)
    rows = len(matrix[0])

    first_row_has_zero = False
    first_col_has_zero = False

    for y in range(0, rows):
        if matrix[0][y] == 0:
            first_row_has_zero = True

    for x in range(0, cols):
        if matrix[x][0] == 0:
            first_col_has_zero = True

    for x in range(1, cols):
        for y in range(1, rows):
            if matrix[x][y] == 0:
                matrix[0][y] = 0
                matrix[x][0] = 0

    for x in range(1, cols):
        if matrix[x][0] == 0:
            wipe_col(matrix, x, rows)

    for y in range(1, rows):
        if matrix[0][y] == 0:
            wipe_row(matrix, y, cols)

    if first_col_has_zero:
        wipe_col(matrix, 0, rows)

    if first_row_has_zero:
        wipe_row(matrix, 0, cols)


def wipe_row(matrix, row, cols):
    for i in range(0, cols):
        matrix[i][row] = 0


def wipe_col(matrix, col, rows):
    for i in range(0, rows):
        matrix[col][i] = 0


w, h = 5, 5
mat = [[1 for x in range(w)] for y in range(h)]
mat[0][0] = 5
mat[4][4] = 4
mat[0][4] = 3
mat[4][0] = 0

print(mat)
zero_matrix(mat)
print(mat)