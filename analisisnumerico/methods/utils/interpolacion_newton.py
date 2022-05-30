import numpy as np
from interpolacion_utils import is_valid

def calcular(a, x, r):
    if not is_valid(x):
        raise Exception("Cada punto en X debe ser unico")
    
    n = len(a) - 1
    p = a[n]
    for i in range(n-1, -1, -1):
        p = p * (r - x[i]) + a[i]
    
    return p

def coeficiente_newton(X, Y):
    if not is_valid(X):
        raise Exception("Cada punto en X debe ser unico")
    
    n = len(X)
    x = np.copy(X)
    a = np.copy(Y)

    for i in range(1, n):
        for j in range(n-1, i-1, -1):
            a[i] = (a[i]-a[i-1]) / (x[i]-x[i-j])
    return a