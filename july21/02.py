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

N = 5
M = 4

random_matrix = create_random_matrix(N, M)
print_matrix(random_matrix)
