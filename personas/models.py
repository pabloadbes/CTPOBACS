from django.db import models
# from ckeditor.fields import RichTextField

class Persona(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=200)
    apellido = models.CharField(verbose_name="Apellido", max_length=200)
    # content = RichTextField(verbose_name="Contenido")
    dni = models.CharField(verbose_name="DNI", max_length=8)
    telefono_area = models.CharField(verbose_name="Código de Área", max_length=4, blank=True, null=True)
    telefono_numero = models.CharField(verbose_name="Número de Teléfono", max_length=8, blank=True, null=True)
    email = models.EmailField(verbose_name="Correo Electrónico", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    created_by = models.IntegerField(verbose_name="Creado por", default=1)
    updated_by = models.IntegerField(verbose_name="Modificado por", default=1)

    class Meta:
        verbose_name = "persona"
        verbose_name_plural = "personas"
        ordering = ['nombre', 'apellido']

    def __str__(self):
        return self.apellido + self.nombre
