from math import *
import sympy as sp

def calcular(fn, x0, x1, tol, nMax):
    answer = {
        "response": "",
        "pasos": []}

    ite = 0
    error = tol + 1

    x = sp.symbols("x")
    f = sp.lambdify(x, fn)
    f0 = f(x0)
    f1 = f(x1)

    x_actual = x1

    while error > tol and ite < nMax:
        x_actual = x1 - f1 * (x1 - x0) / (f1 - f0)
        f_actual = f(x_actual)
        E = abs(x_actual - x1)
        ite += 1
        x0 = x1
        f0 = f1
        x1 = x_actual
        f1 = f_actual

        answer["pasos"].append('iteracion (' + ite + ') x=' + x_actual + ', error=' + error)
        
    answer["response"] = 'Finalizado en iteracion (' + ite + ') x=' + x_actual + ', error=' + error

    return answer
    