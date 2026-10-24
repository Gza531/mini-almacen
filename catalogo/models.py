from django.db import models

# Create your models here.

class Categoria (models.Model): 
    nombre = models.CharField (
        max_length = 50, 
        unique = True,
    )

    estado = models.BooleanField(
        default = True
    )


    class Meta: 
        db_table = "Categorias"
        ordering = ["nombre"]

    def __str__ (self): 
        return f"{self.nombre} - {self.estado}" 
    
    
class Producto (models.Model): 
    nombre = models.CharField(
        max_length = 100, 
    )

    precio = models.DecimalField(
        max_digits=12, 
        decimal_places= 2
    )

    categoria= models.ForeignKey(Categoria, on_delete=models.PROTECT)

    estado = models.BooleanField(
        default = True,
    )

    fecha_alta = models.DateTimeField(
        auto_now_add= True
    )

    class Meta:
        db_table = "Productos"
        ordering = ["nombre"]

    def __str__ (self): 
        return f"{self.nombre} - {self.precio} - {self.categoria}"