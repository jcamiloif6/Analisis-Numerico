import numpy as np
from methods.utils import sustitucionregresiva
from methods.utils import  sustitucionprogresiva

def calcular(A, b):
    answer = {
        "response": "",
        "pasos": []}

    n = len(A[0])
    L = np.eye(n)
    U = np.eye(n)

    for i in range(n):
        U[i][i] = 1

        for j in range(i, n):
            aux = sum(L[i][k] * U[k][j] for k in range(1, i-1))
            U[j][i] = A[j][i] - aux

        for j in range(i, n):
            aux2 = sum(L[i][k] * U[k][j] for k in range(1, i-1))
            L[i][j] = (A[i][j] - aux2) / U[i][i]
        answer["pasos"].append({"A": A,
                                "L": L.tolist(),
                                "U": U.tolist()})

    z = sustitucionprogresiva.calcular(L, b)

    Uz = np.column_stack((U, z))
    x = sustitucionregresiva.calcular(Uz)

    answer["response"] = {"A": A,
                          "L": L.tolist(),
                          "U": U.tolist(),
                          "z": z.tolist(),
                          "x": x.tolist()}

    return answer