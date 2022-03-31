from math import *
import sympy as sp
from sympy import *

def Newton():
    x = sp.symbols("x")
    f = input('Digite la función: ')
    df = sp.diff(f)
    f = sp.lambdify(x, f)
    df = sp.lambdify(x, df)
    x0 = input('Digite el valor inicial: ')
    x0 = float(x0)
    n = input('Digite el máximo número de iteraciones: ')
    n = float(n)
    tol = input('Digite la tolerancia: ')
    tol = float(tol)
    ite = 0
    error = tol + 1
    while error > tol and ite < n:
        x1 = x0 - (f(x0)/df(x0))
        error = abs(x1 - x0)
        ite = ite + 1
        if(error < tol):
            print('x', ite, '=', x1, 'es una buena aproximación de la raíz con tol ', error)
            return
        x0 = x1
        print('x', ite, '=', x1)
        if(ite >= n):
            print("No se encontró raíz en el intervalo")
            return
        
Newton()