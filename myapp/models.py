from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self): # Metodo especial para permitir decirle lo que muestro en el admin de django.
        return self.name # Muestra en la tabla de django por name.
    
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE) # El CASCADE al eliminar el proyecto elimina tambien la tarea.
    done = models.BooleanField(default=False)
    
    def __str__(self): # Metodo especial para permitir decirle lo que muestro en el admin de django.
        return self.title + ' - ' + self.project.name # Muestra en la tabla de django por titulo concatenado por nombre de proyecto.
    
