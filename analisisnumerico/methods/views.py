import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from methods.utils import biseccion, newton, puntofijo, busquedasincrementales, reglafalsa, secante, raicesmultiples, eliminaciongaussianasimple, factorizacionlu, crout, doolittle, cholesky, gaussseidel, jacobi

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. App's backend is up and running.")

@csrf_exempt
def bisection(request):
    body = json.loads(request.body)
    a = float(body['a'])
    b = float(body['b'])
    crit = float(body['crit'])
    fn = str(body['fn'])
    nMax = int(body['nMax'])
    response = biseccion.calcular(a, b, crit, fn, nMax)

    return JsonResponse(response)

@csrf_exempt
def end_newton(request):
    body = json.loads(request.body)
    fn = body['fn']
    x0 = float(body['x0'])
    nMax = float(body['nMax'])
    tol = float(body['tol'])

    response = newton.calcular(fn, x0, nMax, tol)

    return JsonResponse(response)

@csrf_exempt
def punto_fijo(request):
    body = json.loads(request.body)
    gn = body['gn']
    x0 = float(body['x0'])
    nMax = float(body['nMax'])
    tol = float(body['tol'])

    response = puntofijo.calcular(gn, x0, nMax, tol)

    return JsonResponse(response)

@csrf_exempt
def busquedas_incrementales(request):
    body = json.loads(request.body)
    fn = str(body['fn'])
    x0 = float(body['x0'])
    h = float(body['h'])
    nMax = float(body['nMax'])

    response = busquedasincrementales.calcular(fn, x0, h, nMax)

    return JsonResponse(response)

@csrf_exempt
def regla_falsa(request):
    body = json.loads(request.body)
    fn = body['fn']
    a = float(body['a'])
    b = float(body['b'])
    tol = float(body['tol'])
    nMax = float(body['nMax'])

    response = reglafalsa.calcular(fn, a, b, tol, nMax)

    return JsonResponse(response)

@csrf_exempt
def end_secante(request):
    body = json.loads(request.body)
    fn = body['fn']
    x0 = float(body['x0'])
    x1 = float(body['x1'])
    tol = float(body['tol'])
    nMax = float(body['nMax'])

    response = secante.calcular(fn, x0, x1, tol, nMax)

    return JsonResponse(response)

@csrf_exempt
def raices_multiples(request):
    body = json.loads(request.body)
    fn = body['fn']
    x0 = float(body['x0'])
    tol = float(body['tol'])
    nMax = float(body['nMax'])

    response = raicesmultiples.calcular(fn, x0, tol, nMax)

    return JsonResponse(response)

@csrf_exempt
def gauss_simple(request):
    body = json.loads(request.body)
    A = body['A']
    b = body['b']

    response = eliminaciongaussianasimple.calcular(A, b)

    return JsonResponse(response)

@csrf_exempt
def fac_lu_simple(request):
    body = json.loads(request.body)
    A = body['A']
    b = body['b']

    response = factorizacionlu.calcular(A, b)

    return JsonResponse(response)

@csrf_exempt
def end_crout(request):
    body = json.loads(request.body)
    A = body['A']
    b = body['b']

    response = crout.calcular(A, b)

    return JsonResponse(response)

@csrf_exempt
def end_doolittle(request):
    body = json.loads(request.body)
    A = body['A']
    b = body['b']

    response = doolittle.calcular(A, b)

    return JsonResponse(response)

@csrf_exempt
def end_cholesky(request):
    body = json.loads(request.body)
    A = body['A']
    b = body['b']

    response = cholesky.calcular(A, b)

    return JsonResponse(response)

@csrf_exempt
def gauss_seidel(request):
    body = json.loads(request.body)
    A = body['A']
    b = body['b']
    x = body['x']
    tol = body['tol']
    nMax = body['nMax']

    response = gaussseidel.calcular(A, b, x, tol, nMax)

    return JsonResponse(response)

@csrf_exempt
def end_jacobi(request):
    body = json.loads(request.body)
    A = body['A']
    b = body['b']
    x = body['x']
    tol = body['tol']
    nMax = body['nMax']

    response = jacobi.calcular(A, b, x, tol, nMax)

    return JsonResponse(response)
