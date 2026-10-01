def min_max(x: list[float]) -> list[float]:
    """
    Perform Min-Max normalization to scale values to [0, 1].
    
    Args:
        x: A list of numerical values
    
    Returns:
        A new list with values normalized to [0, 1]
    """
    min_max = []

    x_max = max(x)
    x_min = min(x)

    for number in x:
        x_primo = (number - x_min)/(x_max-x_min)
        min_max.append(x_primo)

    return min_max