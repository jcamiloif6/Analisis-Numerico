from numpy import linalg as LNG
import numpy as np

def calcular(A, b, x0, tol, Nmax):
    answer = {
        "response": "",
        "pasos": []}
    D = np.diag(np.diag(A))
    L = np.tril(A) + D
    U = np.triu(A) + D
    T = LNG.inv(D - L) * U
    C = LNG.inv(D - L) * b
    xant = x0
    E = 1000
    cont = 0

    while E>tol and cont<Nmax:
        xact = T * xant + C
        E = LNG.norm(xant - xact)
        xant = xact
        cont += 1
        answer["pasos"].append({"x": xact,
                                "i": cont,
                                "err": E})
    
    answer["response"] = {"x": xact,
                          "i": cont,
                          "err": E}
    