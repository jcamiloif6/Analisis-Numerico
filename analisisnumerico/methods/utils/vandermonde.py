from numpy import linalg as LNG
import numpy as np
from .interpolacion_utils import is_valid
from . import eliminaciongaussianasimple
from numpy.polynomial import chebyshev as C

def calcular(X, Y):
    answer = {
        "response": 0,
        "pasos": []}
    
    if not is_valid(X):
        answer["response"] = "Cada punto en X debe ser unico"
        return answer

    x = np.vander(X)

    gaussian = eliminaciongaussianasimple.calcular(x, Y)
    
    answer["response"] = {"vandermonde": x.tolist(),
                          "a": gaussian["response"]["x"]}

    return answer