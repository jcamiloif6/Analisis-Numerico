from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from methods.utils import biseccion, newton, puntofijo, busquedasincrementales,
                          reglafalsa, secante, raicesmultiples, eliminaciongaussianasimple,
                          crout, doolittle, gaussseidel, jacobi

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. App's backend is up and running.")

def bisection(request):
    a = float(request.GET['a'])
    b = float(request.GET['b'])
    crit = float(request.GET['crit'])
    fn = request.GET['fn']

    response = biseccion.calcular(a, b, crit, fn)

    return JsonResponse(response)

def newton(request):
    fn = request.GET['fn']
    x0 = float(request.GET['x0'])
    n = float(request.GET['n'])
    tol = float(request.GET['tol'])

    response = newton.calcular(fn, x0, n, tol)

    return JsonResponse(response)

def puntofijo(request):
    gn = request.GET['gn']
    x0 = float(request.GET['x0'])
    n = float(request.GET['n'])
    tol = float(request.GET['tol'])

    response = puntofijo.calcular(gn, x0, n, tol)

    return JsonResponse(response)

def busquedasincrementales(request):
    fn = request.GET['fn']
    x0 = float(request.GET['x0'])
    h = float(request.GET['h'])
    nMax = float(request.GET['nMax'])

    response = busquedasincrementales.calcular(gn, x0, h, nMax)

    return JsonResponse(response)

def reglafalsa(request):
    fn = request.GET['fn']
    a = float(request.GET['a'])
    b = float(request.GET['b'])
    tol = float(request.GET['tol'])
    nMax = float(request.GET['nMax'])

    response = reglafalsa.calcular(fn, a, b, tol, nMax)

    return JsonResponse(response)

def secante(request):
    fn = request.GET['fn']
    x0 = float(request.GET['x0'])
    x1 = float(request.GET['x1'])
    tol = float(request.GET['tol'])
    nMax = float(request.GET['nMax'])

    response = secante.calcular(fn, x0, x1, tol, nMax)

    return JsonResponse(response)

def raicesmultiples(request):
    fn = request.GET['fn']
    df = request.GET['df']
    d2f = request.GET['d2f']
    x0 = float(request.GET['x0'])
    tol = float(request.GET['tol'])
    nMax = float(request.GET['nMax'])

    response = raicesmultiples.calcular(fn, df, d2f, x0, tol, nMax)

    return JsonResponse(response)

def gauss_simple(request):
    A = request.GET['A']
    b = request.GET['b']

    response = eliminaciongaussianasimple.calcular(A, b)

    return JsonResponse(response)

def crout(request):
    A = request.GET['A']
    b = request.GET['b']

    response = crout.calcular(A, b)

    return JsonResponse(response)

def doolittle(request):
    A = request.GET['A']
    b = request.GET['b']

    response = doolittle.calcular(A, b)

    return JsonResponse(response)

def cholesky(request):
    A = request.GET['A']
    b = request.GET['b']

    response = cholesky.calcular(A, b)

    return JsonResponse(response)

def gauss_seidel(request):
    A = request.GET['A']
    b = request.GET['b']
    x = request.GET['x']
    tol = request.GET['tol']
    nMax = request.GET['nMax']

    response = gaussseidel.calcular(A, b, x, tol, nMax)

    return JsonResponse(response)

def jacobi(request):
    A = request.GET['A']
    b = request.GET['b']
    x = request.GET['x']
    tol = request.GET['tol']
    nMax = request.GET['nMax']

    response = jacobi.calcular(A, b, x, tol, nMax)

    return JsonResponse(response)
