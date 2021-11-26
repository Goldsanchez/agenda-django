from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Agenda(models.Model):

    creador = models.ForeignKey(User, related_name="creador", on_delete=models.CASCADE, max_length=50)
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)

    class Meta:
        ordering = ('nombre',)
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"

    def __str__(self):
        return self.nombre