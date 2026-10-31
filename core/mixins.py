from rest_framework import status
from rest_framework.response import Response 

class BajaLogicaMixin: 

    def destroy (self, request, *args, **kwargs):
        objeto = self.get_object()

        objeto.estado = False

        objeto.save(update_fields=["estado"])

        return Response(status=status.HTTP_204_NO_CONTENT)


class FiltroEstadoMixin: 

    def get_queryset(self):
        qs = super().get_queryset()
        estado = self.request.query_params.get("estado")
        if estado in ("true", "1"):
            qs = qs.filter(estado=True)
        elif estado in ("false", "0"):
            qs = qs.filter(estado=False)
        return qs

class FiltroNombreMixin:

    def get_queryset(self):
        qs = super().get_queryset()

        search = self.request.query_params.get("search")

        if search:
            qs = qs.filter(nombre__icontains=search)

        return qs