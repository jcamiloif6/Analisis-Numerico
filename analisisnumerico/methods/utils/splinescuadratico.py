import numpy as np
from numpy import linalg as LNG
import sympy as sym
from .interpolacion_utils import is_valid


def calcular(X, Y):
    if not is_valid(X):
        raise Exception("Cada punto en X debe ser unico")

    n = len(X) - 1
    m = 3 * n
    cont = 0
    contx = 0
    A = np.zeros((m, m))
    b = np.zeros(m)

    A[0][0] = X[contx]**2
    A[0][1] = X[contx]**1
    A[0][2] = 1
    for i in range(1, 2*n):
        A[i][cont*3] = X[contx]**2
        A[i][cont*3 + 1] = X[contx]**1
        A[i][cont*3 + 2] = 1
        b[i] = Y[contx]
        if (i % 2) == 0:
            contx += 1
        else:
            cont += 1
    cont = 0
    contx = 1

    for i in range(n-1):
        A[2*n+1][cont*3] = 2*X[contx]
        A[2*n+1][cont*3 + 1] = -1
        cont += 1
        A[2*n+1][cont*3] = 2*X[contx]
        A[2*n+1][cont*3 + 1] = -1
        contx += 1
        b[2*n+1] = 0
    A[m-1][0] = 2
    b[m-1] = 0
    print(b)
    x = LNG.solve(A, b)

    return {"x": x}


    # x = sym.Symbol("x")

    # X = np.copy(X)
    # Y = np.copy(Y)
    # n = X.size
    # y = [(Y[i//2]if i % 2 == 0 else Y[(i)//2]) if i <=
    #      2*(n-1) else 0 for i in range(1, 3*(n-1) + 1)]

    # tabla = np.zeros([3*(n-1), 3*(n-1)])

    # for i in range(n-1):
    #     tabla[2*(i + 1) - 2][3*i] = tabla[2*(i + 1) - 1][3*i] = 1
    #     tabla[2*(i + 1) - 2][3*i + 1] = X[i]
    #     tabla[2*(i + 1) - 2][3*i + 2] = X[i]**2
    #     tabla[2*(i + 1) - 1][3*i + 1] = X[i + 1]
    #     tabla[2*(i + 1) - 1][3*i + 2] = X[i + 1]**2

    # for i in range(n-2):
    #     tabla[2*(n-1) + i][3*i + 1] = 1
    #     tabla[2*(n-1) + i][3*i + 4] = -1
    #     tabla[2*(n-1) + i][3*i + 2] = 2*X[i + 1]
    #     tabla[2*(n-1) + i][3*i + 5] = -2*X[i + 1]

    # tabla[3*(n-1) - 1][2] = 2

    # tabla = np.linalg.inv(tabla)
    # coef = np.matmul(tabla, y)
    # p = []
    # cont = 0
    # for j in range(n-1):
    #     pj = coef[cont] + coef[cont+1] * x + coef[cont+2]*x**2
    #     cont = cont+3
    #     p.append(pj)
    
    # for i in p:
    #     print(eval(i))

    # return {"p": str(p)}
