import numpy as np

def calcular(M):
    n = len(M[0])
    x = np.zeros(n)

    x[n-1] = M[n-1][n] / M[n-1][n-1]
    for i in range(n-1, -1, -1):
        aux = M[i][n]
        for j in range(i+1, n):
            aux =- x[j] * M[i][j]
        x[i] = aux / M[i][i]

    return x