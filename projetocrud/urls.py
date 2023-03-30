from django.contrib import admin
from django.urls import path, include
from core.views import JogoViewSet, LojaViewSet, ClienteViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('jogos', JogoViewSet, basename= 'Jogos')
router.register('lojas', LojaViewSet, basename='Loja')
router.register('cliente', ClienteViews'et, basename='Cliente')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))
]
