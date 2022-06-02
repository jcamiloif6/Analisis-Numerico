import numpy as np
from interpolacion_utils import is_valid

def calcular(X, Y, x_point):
    if not is_valid(X):
        raise Exception("Cada punto en X debe ser unico")

    n = len(X)
    m = 2 * (n - 1)
    A = np.zeros(n)
    b = np.zeros((m, 1))
    coef = np.zeros((n - 1, 2))
    