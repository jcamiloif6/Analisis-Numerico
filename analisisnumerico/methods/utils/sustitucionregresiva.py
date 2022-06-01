import numpy as np

def calcular(M):
    n = len(M)
    x = np.zeros(n)

    x[n-1] = M[n-1][n] / M[n-1][n-1]
    for i in range(n-1, -1, -1):
        sum = 0
        for j in range(i+1, n):
            sum += x[j] * M[i][j]
        x[i] = (M[i][n] - sum )/ M[i][i]

    return x