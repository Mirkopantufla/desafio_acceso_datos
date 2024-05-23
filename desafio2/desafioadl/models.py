from django.db import models

# Create your models here.
class Tarea(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.TextField(default='')
    eliminada = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.descripcion}"

class SubTarea(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.TextField(default='')
    eliminada = models.BooleanField(default=False)
    tarea = models.ForeignKey(Tarea, related_name='subtareas', on_delete=models.CASCADE) #Cambie la idea inicial ya que al crearse cualquier subtarea, requiere de una tarea

    def __str__(self) -> str:
        return f"{self.descripcion}"