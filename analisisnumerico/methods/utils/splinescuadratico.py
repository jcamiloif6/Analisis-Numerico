import numpy as np
from numpy import linalg as LNG
from .interpolacion_utils import is_valid


def calcular(X, Y):
    if not is_valid(X):
        raise Exception("Cada punto en X debe ser unico")

    n = len(X) - 1
    m = 3 * n
    cont = 0
    contx = 0
    A = np.zeros((m, m))
    b = np.zeros(m)

    A[0][0] = X[contx]**2
    A[0][1] = X[contx]**1
    A[0][2] = 1
    for i in range(1, 2*n):
        A[i][cont*3] = X[contx]**2
        A[i][cont*3 + 1] = X[contx]**1
        A[i][cont*3 + 2] = 1
        b[i] = Y[contx]
        if (i % 2) == 0:
            contx += 1
        else:
            cont += 1
    cont = 0
    contx = 1

    for i in range(n-1):
        A[2*n+1][cont*3] = 2*X[contx]
        A[2*n+1][cont*3 + 1] = -1
        cont += 1
        A[2*n+1][cont*3] = 2*X[contx]
        A[2*n+1][cont*3 + 1] = -1
        contx += 1
        b[2*n+1] = 0
    A[m-1][0] = 2
    b[m-1] = 0

    x = LNG.lstsq(A, b, rcond=None)[0]

    return {"A": A.tolist(),
            "b": b.tolist(),
            "x": x.tolist()}
