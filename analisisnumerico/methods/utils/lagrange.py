import numpy as np
from .interpolacion_utils import is_valid

def calcular(X, Y, x_point):
    answer = {
        "response": {},
        "pasos": []}

    if not is_valid(X):
        raise Exception("Cada punto en X debe ser unico")

    n = len(X)
    L = np.zeros(n)

    y_point = 0

    for i in range(n):
        p = 1
        for j in range(n):
            if i != j:
                p = p * (x_point - X[j]) / (X[i] - X[j])
        y_point += p * Y[i]
        answer["pasos"].append(y_point)
    
    answer["response"] = {"y": y_point}
    return answer