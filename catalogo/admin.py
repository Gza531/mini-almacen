from django.contrib import admin
from .models import Categoria, Producto
# Register your models here.


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "estado")

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "categoria", "estado", "precio")
    search_fields = ("nombre",)
    list_filter = ("categoria", "estado")