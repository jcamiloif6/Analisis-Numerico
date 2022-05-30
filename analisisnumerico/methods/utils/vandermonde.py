from numpy import linalg as LNG
import numpy as np
from interpolacion_utils import is_valid

def calcular(X, Y):
    answer = {
        "response": 0,
        "pasos": []}
    
    if not is_valid(X):
        answer["response"] = "Cada punto en X debe ser unico"
        return answer

    x = np.vander(X)
    y = np.vander(Y)

    answer["pasos"].append({"x": x,
                            "y": y})
    
    answer["response"] = LNG.det(x)

    return answer