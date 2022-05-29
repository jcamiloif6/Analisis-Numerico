from math import *
import sympy as sp

def calcular(fn, a, b, tol, nMax):
    answer = {
        "response": "",
        "pasos": []}

    ite = 0
    error = tol + 1

    x = sp.symbols("x")
    f = sp.lambdify(x, fn)
    fa = f(a)
    fb = f(b)
    pm=(fb * a - fa * b) / (fb - fa)
    fpm=f(pm)

    while error > tol and ite < nMax:
        if fa * fpm < 0:
            b = pm
        else:
            a = pm
        p0 = pm
        pm = (f(b) * a - f(a) * b) / (f(b) - f(a))
        fpm = f(pm)
        error = abs(pm - p0)

        answer["pasos"].append('iteracion (' + ite + ') x=' + pm + ', error=' + error)

        ite += 1
        
    answer["response"] = 'Finalizado en iteracion (' + ite + ') x=' + pm + ', error=' + error

    return answer