from methods.utils import sustitucionregresiva

def calcular(A, b):
    answer = {
        "response": "",
        "pasos": []}
    n = len(A[0])
    M=[A, b]

    for i in range(n):
        if M[i][i] == 0:
            answer["response"] = "No se puede dividir por cero."
            return answer
        for j in range(i+1, n):
            r = M[j][i]/M[i][i]

            for k in range(n+1):
                M[j][k] = M[j][k] - r * M[i][k]
                answer["pasos"].append(M)
    
    answer["response"] = sustitucionregresiva.calcular(M)

    return answer