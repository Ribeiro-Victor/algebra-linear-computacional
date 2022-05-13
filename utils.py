def read_matrix(file_path):
    with open(file_path, 'r') as f:
        matrix = [[int(num) for num in row.split(' ')] for row in f]
    return matrix

def print_matrix(matrix):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in matrix]))
