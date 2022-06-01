from sympy import symbols, lambdify, sympify

def calcular(fn, x0, x1, tol, nMax):
    answer = {
        "response": "",
        "pasos": []}

    ite = 0
    error_absolution = tol + 1

    x = symbols("x")
    f = lambdify(x, sympify(fn))
    f0 = f(x0)
    f1 = f(x1)

    x_actual = x1

    if f0 == 0:
        answer["response"] = "x0=" + str(x0) +" es raiz"
        return answer
    
    while error_absolution > tol and ite < nMax:
        x_actual = x1 - f1 * (x1 - x0) / (f1 - f0)
        f_actual = f(x_actual)
        
        # error absoluto
        error_absolution = abs(x_actual - x1)

        # error relativo
        error_relativo = abs((x_actual - x1) / x_actual)
        ite += 1
        x0 = x1
        f0 = f1
        x1 = x_actual
        f1 = f_actual

        answer["pasos"].append('iteracion (' + str(ite) + ') x= ' + str(x_actual) + ', error_absolution= ' + str(error_absolution) + " error_relativo= " + str(error_relativo))
        
    answer["response"] = 'Finalizado en iteracion (' + str(ite) + ') x= ' + str(x_actual) + ', error_absolution= ' + str(error_absolution) + " error_relativo= " + str(error_relativo)

    return answer
    