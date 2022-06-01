from sympy import symbols, lambdify, sympify, diff

def calcular(fn, x0, tol, nMax):
    answer = {
        "response": "",
        "pasos": []}

    ite = 0
    error_absolution = tol + 1

    x = symbols("x")
    f = lambdify(x, sympify(fn))
    df = diff(fn)
    d2f = diff(df)
    dfn = lambdify(x, sympify(df))
    d2fn = lambdify(x, sympify(d2f))

    x_anterior = x0
    f_anterior = f(x_anterior)

    while error_absolution > tol and ite < nMax:
        x_actual = x_anterior - f_anterior * dfn(x_anterior) / (dfn(x_anterior) ** 2 - f_anterior * d2fn(x_anterior))
        f_actual = f(x_actual)
        
        # error absoluto
        error_absolution = abs(x_actual - x_anterior)

        # error relativo
        error_relativo = abs((x_actual - x_anterior) / x_actual)

        ite += 1
        x_anterior = x_actual
        f_anterior = f_actual

        answer["pasos"].append('iteracion (' + str(ite) + ') x=' + str(x_actual) + ', error relativo de ' + str(error_relativo) + " y error absoluto de " + str(error_absolution))
        
    answer["response"] = 'Finalizado en iteracion (' + str(ite) + ') x=' + str(x_actual) + ', error relativo de ' + str(error_relativo) + " y error absoluto de " + str(error_absolution)

    return answer
