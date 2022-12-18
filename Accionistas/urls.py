from django.urls import path, include

from Accionistas import views as app

urlpatterns = [
    path('', app.MostrarInicio),
    path('api/', app.ControladorAPI),
]
