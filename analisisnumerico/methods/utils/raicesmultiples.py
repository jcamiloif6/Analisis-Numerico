from math import *
import sympy as sp

def calcular(fn, df, d2f, x0, tol, nMax):
    answer = {
        "response": "",
        "pasos": []}

    ite = 0
    error = tol + 1

    x = sp.symbols("x")
    f = sp.lambdify(x, fn)
    dfn = sp.lambdify(x, df)
    d2fn = sp.lambdify(x, d2f)

    x_anterior = x0
    f_anterior = f(x_anterior)


    while error > tol and ite < nMax:
        x_actual = x_anterior - f_anterior * dfn(x_anterior) / (dfn(x_anterior) ** 2 - f_anterior * d2fn(x_anterior));
        f_actual = f(x_actual)
        E = abs(x_actual - x_anterior)
        ite += 1
        x_anterior = x_actual
        f_anterior = f_actual

        answer["pasos"].append('iteracion (' + ite + ') x=' + x_actual + ', error=' + error)
        
    answer["response"] = 'Finalizado en iteracion (' + ite + ') x=' + x_actual + ', error=' + error

    return answer
