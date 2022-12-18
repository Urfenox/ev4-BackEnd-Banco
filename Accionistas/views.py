from django.shortcuts import render, HttpResponse
from .models import Accionista

# Create your views here.

def MostrarInicio(request):
    accionistas = Accionista.objects.all()
    data = {'accionistas':accionistas}
    # print("\n" + str(accionistas[1].nombre))
    return render(request, 'Accionistas\index.html', data)

def ControladorAPI(request):
    return HttpResponse("<h1>UPS. Esto no esta listo aun.</h1>")
