from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name='index'),
    path("hola/", views.view1, name='hola'),
]