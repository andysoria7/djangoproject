# from django.shortcuts import render
from django.http import HttpResponse
from .models import Project,Task
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateNewTask, CreateNewProject

# Create your views here.
def index(request):
    title = 'Django Course!!'
    return render(request,'index.html', {
        'title': title # Mostrara djangoCourse
        }) # Para redireccionar a templates html.
    
def hello(request, username):
    return HttpResponse('<h2>Hello %s</h2>' % username)

def about(request):
    username = 'Andy'
    return render(request,'about.html', {
        'username': username
        
    })

def projects(request):
    #projects = list(Project.objects.values()) # Me devuelve una lista de proyectos.
    projects = Project.objects.all()
    return render(request,'projects/projects.html', {
        'projects': projects
    })

def tasks(request):
    #task = Task.objects.get(title=title) # Busca por titulo.
    tasks = Task.objects.all()
    return render(request,'tasks/tasks.html', {
        'tasks': tasks
    })
    
def create_task(request):
    # Renderizo la interface (muestro o obtiene los datos).
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {
            'form': CreateNewTask()
    })
    else:
        # Guardar los datos o insertarlos.
        Task.objects.create(title=request.POST['title'], 
        description=request.POST['description'], project_id=2)
        return redirect('tasks')
    
def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
            'form': CreateNewProject()
    })
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect('projects')
    
def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    return render(request,'projects/detail.html', {
        'project': project,
        'tasks': tasks
    })
        
    
    
        
    
    
    
    
    
    
    
