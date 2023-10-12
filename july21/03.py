import random

def create_random_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = [random.randint(-10, 10) for _ in range(cols)]
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        for num in row:
            print(num, end='\t')
        print()

def calculate_row_odd_sum(matrix):
    row_sums = []
    for row in matrix:
        row_sum = sum(num for num in row if num % 2 != 0)
        row_sums.append(row_sum)
    return row_sums

def calculate_column_odd_sum(matrix):
    col_sums = [0] * len(matrix[0])
    for row in matrix:
        for j, num in enumerate(row):
            if num % 2 != 0:
                col_sums[j] += num
    return col_sums


N = 5
M = 4

random_matrix = create_random_matrix(N, M)

print("Матрица:")
print_matrix(random_matrix)

row_sums = calculate_row_odd_sum(random_matrix)

print("Суммы нечётных элементов в каждой строке:", row_sums)

column_sums = calculate_column_odd_sum(random_matrix)

print("Суммы нечётных элементов в каждом столбце:", column_sums)
