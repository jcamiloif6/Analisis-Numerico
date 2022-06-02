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
    U = np.eye(n)

    for i in range(n):
        U[i, i] = sqrt(M[i, i])
        U[i, i+1:] = M[i, i+1:] / float(U[i, i])
        for j in range(i+1, n):
            M[j, j:] = M[j, j:] - U[i, j] * U[i, j:]
        
        answer["pasos"].append({"A": A,
                                "L": np.transpose(U).tolist(),
                                "U": U.tolist()})

    L = np.transpose(U)

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