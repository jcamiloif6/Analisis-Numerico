import numpy as np

def calcular(A, b):
    answer = {
        "response": "",
        "pasos": []}

    n = len(M[0])
    L = np.eye(n)
    U = np.eye(n)

    for i in range(n):
        U[i][i] = 1

        for j in range(i, n):
            aux = sum(L[i][k] * U[k][j] for k in range(1, i-1))
            U[j][i] = A[j][i] - aux

        for j range(i, n):
            aux2 = sum(L[i][k] * U[k][j] for k in range(1, i-1))
            L[i][j] = (A[i][j] - aux2) / U[k][k]
        answer["pasos"].append({"M": M,
                                "L": L,
                                "U": U})

    z = sustitucionprogresiva.calcular([L, b])
    x = sustitucionregresiva.calcular([U, z])

    answer["response"] = {"M": M,
                          "L": L,
                          "U": U,
                          "z": z,
                          "x": x}

    return answer