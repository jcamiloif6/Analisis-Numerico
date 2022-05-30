import numpy as np

def calcular(M):
    n = len(M[0])
    z = np.zeros(n)

    z[0] = M[0][n+1] / M[0][0]
    for i in range(n-1, -1, -1):
        z[i] = z[i] / M[i][i]
        for j in range(i+1, -1, -1):
            z[i] -= z[i] * M[i][j]
    return z