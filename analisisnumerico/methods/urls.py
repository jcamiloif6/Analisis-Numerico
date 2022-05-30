from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bisection', views.bisection, name='bisection'),
    path('newton', views.newton, name='newton'),
    path('puntofijo', views.puntofijo, name='puntofijo'),
    path('busquedasincrementales', views.busquedasincrementales, name='busquedasincrementales'),
    path('reglafalsa', views.reglafalsa, name='reglafalsa'),
    path('secante', views.secante, name='secante'),
    path('raicesmultiples', views.raicesmultiples, name='raicesmultiples'),
    path('gauss-simple', views.gauss_simple, name='gauss_simple'),
    path('factorizacion-lu-simple', views.fac_lu_simple, name='fac_lu_simple'),
    path('crout', views.crout, name='crout'),
    path('doolittle', views.doolittle, name='doolittle'),
    path('cholesky', views.cholesky, name='cholesky'),
    path('gauss-seidel', views.gauss_seidel, name='gauss_seidel'),
    path('jacobi', views.jacobi, name='jacobi'),
]