import numpy as np

def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    X = np.array(X)
    y = np.array(y)

    #X = np.c_[np.ones((X.shape[0], 1)), X]

    X_t = X.T
    XX_t = X_t @ X
    XX_t_inv = np.linalg.inv(XX_t)

    theta = XX_t_inv@X_t@y
    return theta