from math import *
import sympy as sp
from sympy import *

def calcular(fn, x0, n, tol):
    answer = {
        "response": "",
        "pasos": []}

    ite = 0
    error = tol + 1

    x = sp.symbols("x")
    df = sp.diff(fn)
    f = sp.lambdify(x, fn)
    df = sp.lambdify(x, df)
    
    while error > tol and ite < n:
        x1 = x0 - (f(x0)/df(x0))
        error = abs(x1 - x0)
        ite = ite + 1
        if(error < tol):
            answer["pasos"].append('x' + ite + '=' + x1 + 'es una buena aproximación de la raíz con tol ' + error)
            return answer
        x0 = x1
        answer["response"] = 'x' + ite + '=' + x1
        if(ite >= n):
            answer["response"] = "No se encontró raíz en el intervalo"
            return answer
