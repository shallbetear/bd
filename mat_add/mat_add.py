def read_matrix_from_file(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        matrix = [list(map(int, line.split())) for line in lines]
    return matrix

def write_matrix_to_file(file_name, matrix):
    with open(file_name, 'w') as f:
        for row in matrix:
            f.write(' '.join(map(str, row)) + '\n')

def matrix_add(A, B):
    return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

A = read_matrix_from_file('matrix_A.txt')
B = read_matrix_from_file('matrix_B.txt')

if len(A)!=len(B) or len(A[0])!=len(B[0]):
    print("Matrix dimensions are not compatible for addition!")
else:
    result = matrix_add(A, B)
    write_matrix_to_file('result_matrix.txt', result)
    print("Matrix addition result has been written to result_matrix.txt")
