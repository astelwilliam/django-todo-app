# tasks/models.py
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# tasks/models.py

CATEGORY_CHOICES = [
    ('Work', 'Work'),
    ('Study', 'Study'),
    ('Personal', 'Personal'),
    ('Other', 'Other'),
]

PRIORITY_CHOICES = [
    ('Low', 'Low'),
    ('Medium', 'Medium'),
    ('High', 'High'),
]

user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks', null=True, blank=True)



# tasks/models.py

class Task(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Other')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
    due_date = models.DateTimeField(null=True, blank=True)
    done = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    shared_with = models.ManyToManyField(User, related_name='shared_tasks', blank=True)
    
class SubTask(models.Model):
    parent = models.ForeignKey(Task, related_name='subtasks', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
    due_date = models.DateTimeField(null=True, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Other')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subtasks')  # different name!
    done = models.BooleanField(default=False)
    

    def is_overdue(self):
        if self.due_date and self.due_date < timezone.now() and not self.done:
            return True
        return False

    def __str__(self):
        return self.title
