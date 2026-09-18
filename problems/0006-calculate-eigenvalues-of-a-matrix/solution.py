import math

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    eigenvalues = []

    det = matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]    
    tr = matrix[0][0]+matrix[1][1]
    delta = tr**2 - 4 * det

    eigval_1 = (tr - math.sqrt(delta))/2
    eigval_2 = (tr + math.sqrt(delta))/2

    eigenvalues.append(eigval_2)
    eigenvalues.append(eigval_1)
    
    return eigenvalues