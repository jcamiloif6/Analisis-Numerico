from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bisection', views.bisection, name='bisection'),
    path('newton', views.end_newton, name='end_newton'),
    path('punto-fijo', views.punto_fijo, name='punto_fijo'),
    path('busquedas-incrementales', views.busquedas_incrementales, name='busquedas_incrementales'),
    path('regla-falsa', views.regla_falsa, name='regla_falsa'),
    path('secante', views.end_secante, name='end_secante'),
    path('raices-multiples', views.raices_multiples, name='raices_multiples'),
    path('gauss-simple', views.gauss_simple, name='gauss_simple'),
    path('factorizacion-lu-simple', views.fac_lu_simple, name='fac_lu_simple'),
    path('crout', views.end_crout, name='end_crout'),
    path('doolittle', views.end_doolittle, name='end_doolittle'),
    path('cholesky', views.end_cholesky, name='end_cholesky'),
    path('gauss-seidel', views.gauss_seidel, name='gauss_seidel'),
    path('jacobi', views.end_jacobi, name='end_jacobi'),
    path('vandermonde', views.end_vandermonde, name='end_vandermonde'),
    path('interpolacion-newton', views.interpolacion_newton, name='interpolacion_newton'),
    path('lagrange', views.end_lagrange, name='end_lagrange'),
    path('splines-cuadratico', views.splines_cuadratico, name='splines_cuadratico'),
]