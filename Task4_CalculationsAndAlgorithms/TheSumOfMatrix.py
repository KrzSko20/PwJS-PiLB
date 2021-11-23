import random


def matrix_generator(matrix_x, matrix_y):
    matrix = [[random.randint(0, 100) for x in range(matrix_x)] for y in range(matrix_y)]
    
    return matrix


def matrix_sum(matrix1, matrix2):
    matrix_x = len(matrix1[0])
    matrix_y = len(matrix1)
    matrix = [[0 for x in range(matrix_x)] for y in range(matrix_y)]

    if matrix_x == len(matrix2[0]) and matrix_y == len(matrix2):
        for i in range(0, matrix_x):
            for j in range(0, matrix_y):
                matrix[i][j] = matrix1[i][j] + matrix2[i][j]

    return matrix


def main():
    matrix1 = matrix_generator(128, 128)
    matrix2 = matrix_generator(128, 128)

    matrix3 = matrix_sum(matrix1, matrix2)

    print(matrix1)
    print(matrix2)
    print(matrix3)


if __name__ == '__main__':
    main()
