# Sirve para que nuestra aplicacion pueda añadir determinados modelos al panel de administrador.
from django.contrib import admin
from .models import Project, Task

# Register your models here.
admin.site.register(Project) # Registrar nuestro modelo de la clase Project.
admin.site.register(Task) # Registrar nuestro modelo de la clase Task.
