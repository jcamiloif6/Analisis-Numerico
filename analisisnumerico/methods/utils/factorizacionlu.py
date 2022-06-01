import numpy as np
from methods.utils import sustitucionregresiva
from methods.utils import  sustitucionprogresiva

def calcular(A, b):
    answer = {
        "response": "",
        "pasos": []}
    
    m = len(A)
    n = len(A[0])
    L= np.zeros((n,m))
    U = np.zeros((n, m))
    A = np.array(A)
    M = A

    for i in range(n):
        L[i][i] = 1
        for j in range(i+1, n):
            if M[i][i] == 0:
                answer["response"] = "No se puede dividir por cero."
                return answer
            r = M[j][i] / M[i][i]
            L[j][i] = r
            for k in range(i+1, n):
                M[j][k] -= r * M[i][k]

            for k in range(i, n):
                U[i][k] = M[i][k]

        answer["pasos"].append({"M": M.tolist(),
                                "L": L.tolist(),
                                "U": U.tolist()})

    z = sustitucionprogresiva.calcular(L, b)

    Uz = np.column_stack((U, z))
    x = sustitucionregresiva.calcular(Uz)

    answer["response"] = {"M": M.tolist(),
                          "L": L.tolist(),
                          "U": U.tolist(),
                          "z": z.tolist(),
                          "x": x.tolist()}
    return answer