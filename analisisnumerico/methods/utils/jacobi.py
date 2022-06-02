from numpy import linalg as LNG
import numpy as np

def calcular(A, b, x0, tol, Nmax):
    answer = {
        "response": "",
        "pasos": []}
    n = len(A)
    m = len(A[0])
    
    diag = np.diag(A)
    D = np.zeros((n, m))
    for i in range(n):
        D[i,i]= diag[i]

    L = -np.tril(A) + D
    U = -np.triu(A) + D
    T = np.matmul(LNG.inv(D),(L+U))

    auto_valores, _ = LNG.eig(T)
    auto_valores = abs(auto_valores)

    for i in auto_valores:
        if i >= 1:
            answer["response"] = "El método no converge"
            return answer
            
    C= np.matmul(np.linalg.inv(D),b)
    
    xant = x0
    E = 1000
    cont = 0

    while E>tol and cont<Nmax:
        xact= np.matmul(T, xant) + C
        E = np.amax(np.array(abs(xact - xant)))
        xant = xact
        cont += 1
        answer["pasos"].append({"i": cont,
                                "x": xact.tolist(),
                                "err": E})
    
    answer["response"] = {"x": xact.tolist(),
                          "i": cont,
                          "err": E}
    return answer
    