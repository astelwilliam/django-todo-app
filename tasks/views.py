from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

# Home page — show all tasks
def index(request):
    tasks = Task.objects.all().order_by('-id')  # newest first
    return render(request, 'tasks/index.html', {'tasks': tasks})

# Add a new task
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:  # make sure it's not empty
            Task.objects.create(title=title)
    return redirect('index')

# Toggle a task's completion status
def toggle_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed
    task.save()
    return redirect('index')

# Delete a task
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('index')
