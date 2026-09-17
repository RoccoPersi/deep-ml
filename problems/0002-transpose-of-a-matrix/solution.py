def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """

    row = len(a)
    col = len(a[0])

    traspose = [[a[i][j] for i in range(row)] for j in range(col)]

    return traspose