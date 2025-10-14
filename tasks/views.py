from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.utils import timezone

def index(request):
    tasks = Task.objects.all().order_by('-priority', 'due_date')
    return render(request, 'tasks/index.html', {'tasks': tasks})

def add_task(request):
    if request.method == "POST":
        title = request.POST.get('title')
        category = request.POST.get('category')
        due_date = request.POST.get('due_date')
        priority = request.POST.get('priority')

        Task.objects.create(
            title=title,
            category=category,
            due_date=due_date if due_date else None,
            priority=priority
        )
    return redirect('index')


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