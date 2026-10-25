from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ProductoViewSet, CategoriaViewSet

router= DefaultRouter()
router.register("productos", ProductoViewSet, basename="producto")
router.register("categorias", CategoriaViewSet, basename="categoria")


urlpatterns = [
    path("" , include(router.urls)),
]