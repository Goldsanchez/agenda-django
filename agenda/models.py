from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.
class Agenda(models.Model):

    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")

    creador = models.ForeignKey(User, related_name="creador", on_delete=models.CASCADE, max_length=50)
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=16, validators = [phoneNumberRegex], unique=True)

    class Meta:
        ordering = ('nombre',)
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"

    def __str__(self):
        return self.nombre