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


def find_max_min_in_rows(matrix):
    max_in_rows = [max(row) for row in matrix]
    min_in_rows = [min(row) for row in matrix]
    return max_in_rows, min_in_rows


def find_max_min_in_columns(matrix):
    max_in_cols = [max(col) for col in zip(*matrix)]
    min_in_cols = [min(col) for col in zip(*matrix)]
    return max_in_cols, min_in_cols


N = 5
M = 4

random_matrix = create_random_matrix(N, M)

print("Матрица:")
print_matrix(random_matrix)

max_in_rows, min_in_rows = find_max_min_in_rows(random_matrix)

for i in range(N):
    print(f"Максимальный элемент в строке {i + 1}: {max_in_rows[i]}")
    print(f"Минимальный элемент в строке {i + 1}: {min_in_rows[i]}")

max_in_cols, min_in_cols = find_max_min_in_columns(random_matrix)

for j in range(M):
    print(f"Максимальный элемент в столбце {j + 1}: {max_in_cols[j]}")
    print(f"Минимальный элемент в столбце {j + 1}: {min_in_cols[j]}")
