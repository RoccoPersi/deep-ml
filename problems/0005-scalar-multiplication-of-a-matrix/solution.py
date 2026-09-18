def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	result = []
	for i in range(len(matrix)):
		temp = []
		for j in range(len(matrix[0])):
			temp.append(matrix[i][j] * scalar)
		result.append(temp)
	
	return result
