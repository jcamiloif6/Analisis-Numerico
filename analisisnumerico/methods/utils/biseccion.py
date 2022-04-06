import numpy as np
from sympy import symbols
from sympy import lambdify
from sympy import sympify

def calcular (a, b, crit, fn):
    answer = {
        "response": "La función no tiene una raíz en el intervalo de " + "x = " + str(a) + " a x = " + str(b),
        "pasos": []}
    
    x = symbols('x')
    f = lambdify(x, sympify(fn))
    i = 0
    ea = 1
    x_anterior = 0

    if f(a) * f(b) < 0:
        while ea > crit:
            xr = (a + b)/2
            ea = abs(xr - x_anterior)
            if f(xr) * f(a) < 0:
                b = xr
            else:
                a = xr
            x_anterior = xr
            answer["pasos"].append("{:^10} {:^10} {:^10} {:^10} {:^10}".format(i, a, b, xr, ea))
            i += 1
        answer["response"] = "El valor de x es " + round(xr, 9) + " con un error de " + ea
    else:
        answer["pasos"].append("{:^10} {:^10} {:^10} {:^10} {:^10}".format("i", "a", "b", "xr", "ea"))
