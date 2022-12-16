from django.urls import path

from Accionistas import views as app

urlpatterns = [
    path('', app.MostrarInicio),
    path('panel/', app.MostrarPanel),
]