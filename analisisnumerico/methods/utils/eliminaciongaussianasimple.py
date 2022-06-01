from methods.utils import sustitucionregresiva
import numpy as np

def calcular(A, b):
    answer = {
        "response": "",
        "pasos": []}
    n = len(A[0])
    M = np.column_stack((A, b))

    for i in range(n):
        if M[i][i] == 0:
            answer["response"] = "No se puede dividir por cero."
            return answer
        for j in range(i+1, n):
            r = M[j][i] / M[i][i]
            for k in range(i, n+1):
                M[j][k] = M[j][k] - r * M[i][k]
        answer["pasos"].append(M.tolist())
    
    answer["response"] = {
        "Ab": M.tolist(),
        "x": sustitucionregresiva.calcular(M).tolist()}

    return answer