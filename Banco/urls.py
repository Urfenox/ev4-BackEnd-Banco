from django.urls import path

from Banco import views as app

urlpatterns = [
    path('', app.MostrarInicio)
]
