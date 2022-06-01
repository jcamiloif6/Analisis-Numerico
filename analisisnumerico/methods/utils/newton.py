from sympy import symbols, lambdify, sympify, diff

def calcular(fn, x0, nMax, tol):
    answer = {
        "response": "",
        "pasos": []}

    ite = 0
    error_absolution = tol + 1

    x = symbols("x")
    df = diff(fn)
    f = lambdify(x, sympify(fn))
    df = lambdify(x, sympify(df))
    
    while error_absolution > tol and ite < nMax:
        x1 = x0 - (f(x0)/df(x0))
        # error absoluto
        error_absolution = abs(x1 - x0)

        # error relativo
        error_relativo = abs((x1 - x0) / x1)

        ite = ite + 1
        if error_absolution < tol:
            answer["response"] = 'x' + str(ite) + '= ' + str(x1) + 'con error relativo de ' + str(error_relativo) + " y error absoluto de " + str(error_absolution)
            # answer["pasos"].append('x' + str(ite) + '=' + str(x1) + 'es una buena aproximación de la raíz con tol ' + str(error))
            return answer
        x0 = x1
        answer["pasos"].append('x' + str(ite) + '=' + str(x1) + ' con relativo de ' + str(error_relativo) + " y error absoluto de " + str(error_absolution))
        
        if ite >= nMax:
            answer["response"] = "No se encontró raíz en el intervalo"
            return answer
