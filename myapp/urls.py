from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'), # con el name, en views al poner el mismo name que pusimos aca en el redirect(), va a redireccionar.
    path('about/',views.about, name='about'),
    path('hello/<str:username>',views.hello , name='hello'),
    path('projects/',views.projects , name='projects'),
    path('projects/<int:id>',views.project_detail , name='project_detail'),
    path('tasks/',views.tasks , name='tasks'), # Se le pasa la url para que busque por titulo de la tarea.
    path('create_task/',views.create_task , name='create_task'),
    path('create_project/',views.create_project , name='create_project'),
    
    
    
]