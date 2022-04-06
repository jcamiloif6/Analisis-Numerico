from math import *
import sympy as sp

def calcular(gn, x0, n, tol):
    answer = {
        "response": "",
        "pasos": []}
    
    x = sp.symbols('x')
    g = sp.lambdify(x,gn)
    ite = 0
    error = tol + 1
    
    while error > tol and ite < n:
        x1 = g(x0)
        error = abs(x1 - x0)
        ite = ite + 1
        if(error < tol):
            answer["pasos"].append('x' + ite + '=' + x1 + 'es punto fijo con tol' + error)
            return answer
        x0 = x1
        answer["response"] = 'x' + ite + '=' + x1
        if(ite >= n):
            answer["response"] = "No se encontró raíz en el intervalo"
            return answer