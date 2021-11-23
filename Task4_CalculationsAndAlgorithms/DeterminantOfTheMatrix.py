import random
import numpy as np


def matrix_generator(matrix_x, matrix_y):
    matrix = [[random.randint(0, 100) for x in range(matrix_x)] for y in range(matrix_y)]

    return matrix


def matrix_determinant(matrix):
    if len(matrix[0]) == len(matrix):
        return np.linalg.det(matrix)
    else:
        return print("Matrix is not square.")


def main():
    matrix = matrix_generator(4, 4)
    print(matrix)

    matrix_det = matrix_determinant(matrix)
    print(matrix_det)


if __name__ == '__main__':
    main()
