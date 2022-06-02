import numpy as np

def reverse_column_stack(M):
    n, _ = M.shape
    A = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            A[i][j] = M[i][j]
    return A

def calcular(A, b):
    answer = {
        "response": {},
        "pasos": []}

    M = np.column_stack((A, b))

    n, _ = M.shape
    P = np.identity(n)
    L = np.identity(n)
    U = M.copy()
    LF = np.eye(n, n)
    for k in range(0, n - 1):
        index = np.argmax(abs(U[k:,k]))
        index = index + k 
        if index != k:
            P = np.identity(n)
            P[[index,k],k:n] = P[[k,index],k:n]
            U[[index,k],k:n] = U[[k,index],k:n] 
            LF = np.dot(P,LF)
        L = np.identity(n)
        for j in range(k+1,n):
            L[j,k] = -(U[j,k] / U[k,k])
            LF[j,k] = (U[j,k] / U[k,k])
        U = np.dot(L,U)
        answer["pasos"].append({"L": LF.tolist(),
                                "U": reverse_column_stack(U).tolist()})

    answer["response"] = {"L": LF.tolist(),
                          "U": reverse_column_stack(U).tolist()}
    
    return answer