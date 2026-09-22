import numpy as np

def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
    x = [0 for i in range(len(b))]
    A = np.array(A)
    b = np.array(b)

    for i in range(A.shape[0]):
        s = 0
        for j in range(A.shape[1]):
            if i == j:
                a = A[i][j]
            else:
                s += abs(A[i][j])

        if abs(a) < s:
            return -1

    for k in range(n):  
        x_new = [0 for _ in range(A.shape[0])]      
        for i in range(A.shape[0]):
            x_new[i] = (b[i] - sum(A[i][j] * x[j] for j in range(A.shape[0]) if j != i)) / A[i][i]

        x = x_new

    return x