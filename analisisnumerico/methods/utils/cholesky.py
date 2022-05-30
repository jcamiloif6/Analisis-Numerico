import numpy as np
from methods.utils import sustitucionregresiva
from methods.utils import  sustitucionprogresiva

def calcular(A, b):
    answer = {
        "response": {},
        "pasos": []}

    n = len(A[0])
    L = np.eye(n)
    U = np.eye(n)

    for i in range(n):
        aux = sum(L[i][k] * U[k][j] for k in range(1, i-1))
        L[i][i] = sqrt(A[i][i] - aux)
        U[i][i] = L[i][i]
        for j in range(i, n):
            aux2 = sum(L[i][k] * U[k][j] for k in range(1, i-1))
            L[j][i] = (A[j][i] - aux2) / U[i][i]

        for j range(i, n):
            aux3 = sum(L[i][k] * U[k][j] for k in range(1, i-1))
            L[i][j] = (A[i][j] - aux3) / L[k][k]
        answer["pasos"].append({"A": A,
                                "L": L,
                                "U": U})
    aux4 = sum(L[n][k] * U[k][n] for k in range(n))
    L[n][n] = sqrt(A[n][n] - aux4)
    U[n][n] = L[n][n]

    z = sustitucionprogresiva.calcular([L, b])
    x = sustitucionregresiva.calcular([U, z])

    answer["response"] = {"A": A,
                          "L": L,
                          "U": U,
                          "z": z,
                          "x": x}

    return answer