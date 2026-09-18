def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	media = []
	if mode == 'column':
		for i in range(len(matrix[0])):
			conta = 0
			somma = 0
			for j in range(len(matrix)):
				conta += 1
				somma += matrix[j][i]
			media.append(somma/conta)
	else:
		for i in range(len(matrix)):
			conta = 0
			somma = 0
			for j in range(len(matrix[0])):
				conta += 1
				somma += matrix[i][j]
			media.append(somma/conta)

	return media