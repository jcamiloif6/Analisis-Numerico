from math import *
import sympy as sp

def calcular(fn, x0, h, nMax):
    answer = {
        "response": "",
        "pasos": []}
    
    x = sp.symbols('x')
    f = sp.lambdify(x, fn)

    x_anterior = x0
    f_anterior = f(x_anterior)

    x_actual = x_anterior + h
    f_actual = f(x_actual)

    ite = 0
    
    while ite < nMax:
        if f_anterior * f_actual < 0:
            answer["response"] = "No se encontró raíz en el intervalo"
            return answer
        answer["pasos"].append('iteracion (' + ite + '): a=' + x_anterior + ', b=' + x_actual)
        x_anterior = x_actual
        f_anterior = f_actual

        x_actual = x_anterior + h
        f_actual = f(x_actual)
        ite += 1
    answer["response"] = 'Finalizado en iteracion (' + ite + '): a=' + x_anterior + ', b=' + x_actual
