def read_matrix(filename):
    with open(filename, 'r') as f:
        return [[int(num) for num in line.split()] for line in f]
