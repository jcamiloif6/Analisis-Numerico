from sympy import symbols, lambdify, sympify

def calcular(gn, x0, nMax, tol):
    answer = {
        "response": "",
        "pasos": []}
    
    x = symbols('x')
    g = lambdify(x, sympify(gn))
    ite = 0
    error_absolution = tol + 1
    
    while error_absolution > tol and ite < nMax:
        x1 = g(x0)

        # error absoluto
        error_absolution = abs(x1 - x0)

        # error relativo
        error_relativo = abs((x1 - x0) / x1)

        ite = ite + 1
        if error_absolution < tol:
            answer["pasos"].append('x' + str(ite) + '=' + str(x1) + ' es punto fijo con error relativo de ' + str(error_relativo) + " y error absoluto de " + str(error_absolution))
            answer["response"] = 'x' + str(ite) + '=' + str(x1)
            return answer
        x0 = x1
        answer["pasos"].append('x' + str(ite) + '=' + str(x1) + ' es punto fijo con error relativo de ' + str(error_relativo) + " y error absoluto de " + str(error_absolution))
        answer["response"] = 'x' + str(ite) + '=' + str(x1)
        if ite >= nMax:
            answer["response"] = "No se encontró raíz en el intervalo"
            return answer