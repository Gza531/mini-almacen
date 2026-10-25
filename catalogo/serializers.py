from decimal import Decimal
from rest_framework import serializers
from .models import Categoria, Producto


class CategoriaSerializer(serializers.ModelSerializer) :

    def validate_nombre (self, valor):

        valor = valor.strip()
        repetidos = Categoria.objects.filter(nombre__iexact=valor)
        if self.instance: 
             repetidos = repetidos.exclude(pk=self.instance.pk)
        if repetidos.exists():
            raise serializers.ValidationError("Ya existe una categoría con ese nombre.")
        return valor


    class Meta:
        model = Categoria
        fields = [
                "id",
                "nombre",
                "estado",
            ]


class ProductoSerializer(serializers.ModelSerializer) :
        categoria_nombre = serializers.CharField(
            source="categoria.nombre",
            read_only=True
        )

        precio = serializers.DecimalField(max_digits=12, decimal_places=2, min_value=Decimal('0.01') )

        class Meta: 
            model = Producto
            fields = [
                "id",
                "nombre",
                "precio",
                "categoria",
                "categoria_nombre",
                "estado",
                 ]