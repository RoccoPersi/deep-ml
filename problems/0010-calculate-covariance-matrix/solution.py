def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    dim_vectors = len(vectors)
    x_dim = []
    res = []
    cov = []

    for dim in range(dim_vectors):
        somma = sum(vectors[dim])
        x_mean = somma/len(vectors[dim])
        centralizzati = []

        for k in range(len(vectors[dim])):
            centralizzati.append(vectors[dim][k] - x_mean)        

        x_dim.append(centralizzati)

    cov = [[0.0] * dim_vectors for _ in range(dim_vectors)]

    for i in range(dim_vectors):
        for j in range(dim_vectors):
            s = sum(x_dim[i][k]*x_dim[j][k] for k in range(len(vectors[0])))
            cov[i][j] = s / (len(x_dim[0])-1)

    return cov