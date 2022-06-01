from sympy import symbols, lambdify, sympify

def calcular(fn, x0, h, nMax):
    answer = {
        "response": "",
        "pasos": []}
    
    x = symbols('x')
    f = lambdify(x, sympify(fn))

    x_anterior = x0
    f_anterior = f(x_anterior)

    x_actual = x_anterior + h
    f_actual = f(x_actual)

    ite = 0
    
    while ite < nMax:
        if f_anterior * f_actual < 0:
            answer["response"] = 'Finalizado en iteracion (' + str(ite) + '): a=' + str(x_anterior) + ', b=' + str(x_actual)
            return answer
        answer["pasos"].append('iteracion (' + str(ite) + '): a=' + str(x_anterior) + ', b=' + str(x_actual))
        x_anterior = x_actual
        f_anterior = f_actual

        x_actual = x_anterior + h
        f_actual = f(x_actual)
        ite += 1
    answer["response"] = "No se encontró raíz en el intervalo"

    return answer