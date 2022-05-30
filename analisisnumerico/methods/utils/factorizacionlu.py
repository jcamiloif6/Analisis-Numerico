import numpy as np
from methods.utils import sustitucionregresiva
from methods.utils import  sustitucionprogresiva

def calcular(M, b):
    answer = {
        "response": "",
        "pasos": []}
    
    n = len(M[0])
    L = np.eye(n)
    U = np.zeros(n)
    M=A

    for i in range(n):
        for j in range(i+1, n):
            if M[j][i] == 0:
                answer["response"] = "No se puede dividir por cero."
                return answer
            r = M[j][i]/M[i][i]
            L[j][i] = r
            for k in range(i, n):
                M[j][k] -= r * M[i][k]
            
        for j in range(i, n):
            U[i][k] = M[i][k]

        for j in range(i+1, n):
            U[i+1][j]=M[i+1][j]
        answer["pasos"].append({"M": M,
                                "L": L,
                                "U": U})
    U[n][n] = M[n][n]

    z = sustitucionprogresiva.calcular([L, b])
    x = sustitucionregresiva.calcular([U, z])

    answer["response"] = {"M": M,
                          "L": L,
                          "U": U,
                          "z": z,
                          "x": x}
    return answer