# Chapter 1 problem 7
import math


def rotate_matrix(matrix: object) -> object:
    cols = len(matrix)

    for level in range(0, math.ceil(cols / 2)):
        first = level
        last = cols - 1 - level
        offset = 0
        for x in range(first, last):
            stored_value = matrix[first][x]
            matrix[first][x] = matrix[last - offset][first]
            matrix[last - offset][first] = matrix[last][last - offset]
            matrix[last][last - offset] = matrix[x][last]
            matrix[x][last] = stored_value
            offset +=1

w, h = 5, 5
mat = [[0 for x in range(w)] for y in range(h)]
mat[0][0] = 5
mat[4][4] = 4
mat[0][4] = 3
mat[4][0] = 2

print(mat)
rotate_matrix(mat)
print (mat)
