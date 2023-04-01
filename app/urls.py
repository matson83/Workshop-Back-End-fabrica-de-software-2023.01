from rest_framework import routers
from app.views import ClienteViewSet,ProdutoViewSet

router = routers.SimpleRouter()
router.register('Cliente',ClienteViewSet,basename='Cliente')
router.register('Produto',ProdutoViewSet,basename='Produto')

urlpatterns = router.urls