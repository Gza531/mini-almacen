from rest_framework import viewsets
from rest_framework.exceptions import ValidationError

from core.mixins import (
    BajaLogicaMixin,
    FiltroEstadoMixin,
    FiltroNombreMixin,
)

from .models import Producto, Categoria
from .serializers import ProductoSerializer, CategoriaSerializer


class ProductoViewSet(
    BajaLogicaMixin,
    FiltroEstadoMixin,
    FiltroNombreMixin,
    viewsets.ModelViewSet
):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        categoria = self.request.query_params.get("categoria")

        if categoria:
            try:
                categoria_id = int(categoria)
            except ValueError:
                raise ValidationError({
                    "categoria": "Debe ser un ID válido."
                })

            qs = qs.filter(categoria_id=categoria_id)

        return qs


class CategoriaViewSet(
    BajaLogicaMixin,
    FiltroEstadoMixin,
    FiltroNombreMixin,
    viewsets.ModelViewSet
):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer