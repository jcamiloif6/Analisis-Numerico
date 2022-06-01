import numpy as np

def calcular(L, b):
    n = len(b)
    z = np.zeros(n)

    for i in range(n):
        z[i] = b[i]
        for j in range(i):
            z[i] = z[i] - (L[i][j] * z[j])
        z[i] = z[i] / L[i][i]
    
    return z