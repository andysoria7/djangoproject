from django import forms # Me permite poder hacer que una clase se extienda para que se convierta en un formulario html.

class CreateNewTask(forms.Form): # Esto es para enviarselo al html.
    title = forms.CharField(label="Titulo de tarea", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
    description = forms.CharField(label = "Descripcion de la tarea", widget=forms.Textarea(attrs={'class': 'input'}))
    
class CreateNewProject(forms.Form):
    name = forms.CharField(label="Nombre del Project", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
    
    
     
    
