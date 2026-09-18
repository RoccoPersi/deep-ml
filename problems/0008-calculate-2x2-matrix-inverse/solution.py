def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    
    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]
    
    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
        (i.e., determinant equals zero)
    """
    # Your code here
    inv_top = []
    inv_bottom = []
    inv = []
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]

    det = a*d - b*c

    if det == 0:
        return None

    d_1 = d/det
    inv_top.append(d_1)
    b_1 = -b/det
    inv_top.append(b_1)

    inv.append(inv_top)

    c_1 = -c/(det)
    inv_bottom.append(c_1)
    a_1 = a/det
    inv_bottom.append(a_1)

    inv.append(inv_bottom)

    return inv