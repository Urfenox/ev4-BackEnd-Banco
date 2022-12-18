from django.shortcuts import render
from .models import Accionista
from .serializer import AccionistaSerializer
from rest_framework import generics, mixins
from rest_framework import viewsets

# Create your views here.

def MostrarInicio(request):
    accionistas = Accionista.objects.all()
    data = {'accionistas':accionistas}
    # print("\n" + str(accionistas[1].nombre))
    return render(request, 'Accionistas\index.html', data)

# API REST
class AccionistaList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Accionista.objects.all()
    serializer_class = AccionistaSerializer

    def get(self, request):
        return self.list(request)
    
    def post(selft, request):
        return self.create(request)

class AccionistaDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Accionista.objects.all()
    serializer_class = AccionistaSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        return self.update(request, pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)

class AccionistaViewSets(viewsets.ModelViewSet):
    queryset = Accionista.objects.all()
    serializer_class = AccionistaSerializer
