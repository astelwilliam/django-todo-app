from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.db.models import Q

@login_required
def index(request):
    tasks = Task.objects.filter(Q(user=request.user) | Q(shared_with=request.user)).order_by('-priority', 'due_date')
    return render(request, 'tasks/index.html', {'tasks': tasks})

@login_required
def task_list(request):
    tasks = Task.objects.filter(Q(user=request.user) | Q(shared_with=request.user)).order_by('-priority', 'due_date')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


@login_required
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
            priority=priority,
            user=request.user
        )
    return redirect('index')


@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.save()
        return redirect('index')
    return render(request, 'tasks/edit_task.html', {'task': task})

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()
    return redirect('index')

from django.shortcuts import redirect, get_object_or_404
from .models import Task

@login_required
def toggle_done(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.done = not task.done  # ✅ Toggle True/False
    task.save()
    return redirect('index')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def share_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        username = request.POST.get('username')
        try:
            user_to_share = User.objects.get(username=username)
            if user_to_share != request.user:
                task.shared_with.add(user_to_share)
        except User.DoesNotExist:
            pass  # Handle error if user doesn't exist
    return redirect('edit_task', task_id=task.id)
