from django.urls import path
from .views import hello_world

urlpatterns = [
    # define la ruta para la vista hello_world.
    path('',hello_world) #cuando se teclee hello/ en el navegador se llama a la funcion hello_world
]