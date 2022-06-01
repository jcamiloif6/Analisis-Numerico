from sympy import symbols, lambdify, sympify

def calcular(fn, a, b, tol, nMax):
    answer = {
        "response": "",
        "pasos": []}

    ite = 0
    error = tol + 1

    x = symbols("x")
    f = lambdify(x, sympify(fn))
    fa = f(a)
    fb = f(b)
    pm=(fb * a - fa * b) / (fb - fa)
    fpm=f(pm)

    while error > tol and ite < nMax:
        if fa * fpm < 0:
            b = pm
        else:
            a = pm
        p0 = pm
        if (f(b) - f(a)) == 0:
            break
        pm = (f(b) * a - f(a) * b) / (f(b) - f(a))
        fpm = f(pm)
        error = abs(pm - p0)

        answer["pasos"].append('iteracion (' + str(ite) + ') x=' + str(pm) + ', error=' + str(error))

        ite += 1
        
    answer["response"] = 'Finalizado en iteracion (' + str(ite) + ') x=' + str(pm) + ', error=' + str(error)

    return answer