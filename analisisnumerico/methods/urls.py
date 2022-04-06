from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bisection', views.bisection, name='bisection'),
    path('newton', views.newton, name='newton'),
]