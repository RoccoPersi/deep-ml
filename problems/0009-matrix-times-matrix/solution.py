def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:


    c = []
    somma = 0 

    n = len(a[0])
    p = len(b)

    m = len(a)
    q = len(b[0])

    #print(f"Numero colonne Matrice A :{n}")
    #print(f"Numero righe Matrice B :{p}")
    if n == p:
        for k in range(m):
            for i in range(n):
                for j in range(p):
                    somma += a[k][j]*b[j][i]
                    print(f"{a[k][j]}*{b[j][i]}")

                c.append(somma)
                somma = 0
    else:
        return -1

    return c