import numpy as np

def calcular(A, b):
    answer = {
        "response": {},
        "pasos": []}

    U = np.copy(A)
    n = len(b)
    b = np.copy(b)
    x = np.zeros(n)

    for k in range(n-1):
        if np.fabs(U[k, k]) < 1.0e-12:

            for i in range(k+1, n):
                if np.fabs(U[i, k]) > np.fabs(U[k, k]):
                    U[[k, i]] = U[[i, k]]
                    b[[k, i]] = b[[i, k]]
                    break
        for i in range(k+1, n):
            if U[i, k] == 0:
                continue

            factor = U[k, k]/U[i, k]
            for j in range(k, n):
                U[i, j] = U[k, j] - U[i, j] * factor
            b[i] = b[k] - b[i] * factor
        answer["pasos"].append({"U":U.tolist()})

    x[n-1] = b[n-1] / U[n-1, n-1]
    for i in range(n-2, -1, -1):
        sum_ax = 0

        for j in range(i+1, n):
            sum_ax += U[i, j] * x[j]

        x[i] = (b[i] - sum_ax) / U[i, i]
        answer["pasos"].append({"x": x.tolist()})

    answer["response"] = {"A": A,
                          "U": U.tolist(),
                          "x": x.tolist()}

    return answer
