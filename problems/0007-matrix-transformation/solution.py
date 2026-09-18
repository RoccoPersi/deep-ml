import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
    A_np = np.array(A)
    T_np = np.array(T)
    S_np = np.array(S)

    det_T = np.linalg.det(T_np)
    det_S = np.linalg.det(S_np)

    if (det_T == 0) | (det_S == 0):
        return -1

    T_inv = np.linalg.inv(T)

    transformed_matrix = T_inv @ A_np @ S_np

    transformed_matrix = transformed_matrix.tolist()

    return transformed_matrix