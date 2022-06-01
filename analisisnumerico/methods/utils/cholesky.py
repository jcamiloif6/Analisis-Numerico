from math import sqrt
import numpy as np
from methods.utils import sustitucionregresiva
from methods.utils import  sustitucionprogresiva

def calcular(A, b):
    answer = {
        "response": {},
        "pasos": []}

    n = len(A[0])
    M = np.copy(A)
    L = np.eye(n)
    U = np.eye(n)

    for i in range(n):
        aux = sum(L[i][k] * U[k][i] for k in range(1, i-1))
        L[i][i] = sqrt(M[i, i] - aux)

        U[i, i] = sqrt(M[i, i])
        U[i, i+1:] = M[i, i+1:] / float(U[i, i])
        for j in range(i+1, n):
            aux2 = sum(L[i][k] * U[k][j] for k in range(1, i-1))
            L[j][i] = (M[j][i] - aux2) / float(U[i][i])

            M[j, j:] = M[j, j:] - U[i, j] * U[i, j:]
        
        answer["pasos"].append({"A": A,
                                "L": L.tolist(),
                                "U": U.tolist()})

    aux4 = sum(L[n-1][k] * U[k][n-1] for k in range(1, n-1))
    L[n-1][n-1] = sqrt(A[n-1][n-1] - aux4)
    # U[n-1][n-1] = L[n-1][n-1]

    # for i in range(n):
    #     aux = sum(L[i][k] * U[k][j] for k in range(1, i-1))
    #     L[i][i] = sqrt(A[i][i] - aux)
    #     U[i][i] = L[i][i]
    #     for j in range(i, n):
    #         aux2 = sum(L[i][k] * U[k][j] for k in range(1, i-1))
    #         L[j][i] = (A[j][i] - aux2) / U[i][i]

    #     for j in range(i, n):
    #         aux3 = sum(L[i][k] * U[k][j] for k in range(1, i-1))
    #         L[i][j] = (A[i][j] - aux3) / L[i][i]
    #     answer["pasos"].append({"A": A,
    #                             "L": L.tolist(),
    #                             "U": U.tolist()})
    # aux4 = sum(L[n-1][k] * U[k][n-1] for k in range(n))
    # L[n-1][n-1] = sqrt(A[n-1][n-1] - aux4)
    # U[n-1][n-1] = L[n-1][n-1]

    z = sustitucionprogresiva.calcular(L, b)

    Uz = np.column_stack((U, z))
    x = sustitucionregresiva.calcular(Uz)

    answer["response"] = {"A": A,
                          "L": L.tolist(),
                          "U": U.tolist(),
                          "z": z.tolist(),
                          "x": x.tolist()
                          }

    return answer