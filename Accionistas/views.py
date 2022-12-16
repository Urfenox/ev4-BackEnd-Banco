from django.shortcuts import render

# Create your views here.

def MostrarInicio(request):
    return render(request, 'Accionistas\index.html')

def MostrarPanel(request):
    return render(request, 'Accionistas\panel.html')
