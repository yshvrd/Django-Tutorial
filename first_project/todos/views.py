# this file is used to define routes 

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed
from .forms import PersonForm, TodoForm
from .models import Todo

# Create your views here.

# takes an http request and gives back and http response
def hello_world_view(request):
    return HttpResponse("Hello World !")

def hello_python_view(request):
    return HttpResponse("Hello Python")

def hello_html_view(request):
    return render(request, 'todos/hello.html')

def hello_path(request, name):
    return HttpResponse(f'Hello {name}')

def post_example(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            job = form.cleaned_data['job']

            return HttpResponse(f"you posted {name}, {age}, {job}")
    else:
        return HttpResponseNotAllowed(['POST'])

def submit_example(request):
    return render(request, 'todos/submit.html')

def submit_django_form(request):
    form = PersonForm()
    return render(request, 'todos/submit_django_form.html', {'form': form})


def template_view(request):
    context = {
        "name": "yash",
        "age": 22,
        "skills": [
            "python",
            "fastapi",
            "docker"
        ]
    }
    return render(request, 'todos/template_demo.html', context)
    
    
def todos_view(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid:
            todo = form.save()
            return HttpResponse('Todo successfully created!')
    else:
        form = TodoForm
        todos = Todo.objects.all()

        return render(request, 'todos/todos.html', { 'form': form ,'todos': todos})
