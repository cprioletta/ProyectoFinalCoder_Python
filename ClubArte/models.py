from django.db import models

# Create your models here.
class Cine(models.Model):
    titulo =models.CharField(max_length=50)
    director =models.CharField(max_length=50)
    id_Cine =models.IntegerField()

    def __str__(self):
        return f"La película agregada:{self.titulo} fue dirigida por {self.director}." \
               f"El ID para encontrarla es {self.id_Cine}"

