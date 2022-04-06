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
]