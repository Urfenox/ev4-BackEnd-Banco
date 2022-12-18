from django.urls import path, include

# from Accionistas import views as app
from Accionistas import views

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('../api', views.AccionistaViewSets)

urlpatterns = [
    path('', views.MostrarInicio),
    path('rest/', include(router.urls)),
    path('api/', views.AccionistaList.as_view()),
    path('api/<int:pk>/', views.AccionistaDetail.as_view())
]
