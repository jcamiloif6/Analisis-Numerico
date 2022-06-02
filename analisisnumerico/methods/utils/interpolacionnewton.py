import sympy as sym
import numpy as np
from .interpolacion_utils import is_valid

def polinomio_newton(a, x, r):
    answer = {
        "response": {},
        "pasos": []}
    
    n = len(a) - 1
    p = a[n]

    for i in range(n-1, -1, -1):
        p = p * (r - x[i]) + a[i]
        answer["pasos"].append({"p": p})

    answer["response"] = {"a": a,
                          "p": p}
    return p

def diferencia_dividida(X, Y):
    answer = {
        "response": {},
        "pasos": []}
    
    # n = len(X)
    # x = np.copy(X)
    # a = np.copy(Y)

    # for i in range(1, n):
    #     for j in range(n-1, i-1, -1):
    #         a[i] = (a[i] - a[i-1]) / (x[i]-x[i-j])

    # answer["response"] = {"a": a.tolist()}

    n = len(Y)
    a = np.zeros([n, n])

    a[:,0] = Y

    for j in range(1,n):
        for i in range(n-j):
            a[i][j] = (a[i+1][j-1] - a[i][j-1]) / (X[i+j] - X[i])
    
    return a

def calcular(X, Y, r):
    response = {"a": [],
                "p": "No hay nuevo punto a encontrar"}
    if not is_valid(X):
        raise Exception("Cada punto en X debe ser unico")

    X = np.copy(X)
    Y = np.copy(Y)
    p = 0

    a_s = diferencia_dividida(X, Y)[0, :]
    response["a"] = a_s.tolist()

    if r is not None:
        p = polinomio_newton(a_s, X, r)
        response["p"] = p
    
    return response