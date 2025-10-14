from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def index(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/index.html', {'tasks': tasks})

from django.shortcuts import redirect

def add_task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        if title:  # check if title is not empty
            Task.objects.create(title=title)
    return redirect("index")


def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.save()
        return redirect('index')
    return render(request, 'tasks/edit_task.html', {'task': task})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('index')

from django.shortcuts import redirect, get_object_or_404
from .models import Task

def toggle_done(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.done = not task.done  # ✅ Toggle True/False
    task.save()
    return redirect('index')