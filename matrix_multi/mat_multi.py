def read_matrix_from_file(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        matrix = [list(map(int, line.split())) for line in lines]
    return matrix

def write_matrix_to_file(file_name, matrix):
    with open(file_name, 'w') as f:
        for row in matrix:
            f.write(' '.join(map(str, row)) + '\n')

def matrix_multiply(A, B):
    result = [[0] * len(B[0]) for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

A = read_matrix_from_file('matrix_A.txt')
B = read_matrix_from_file('matrix_B.txt')

if len(A[0]) != len(B):
    print("Matrix dimensions are not compatible for multiplication!")
else:
    result = matrix_multiply(A, B)
    write_matrix_to_file('result_matrix.txt', result)
    print("Matrix multiplication result has been written to result_matrix.txt")
