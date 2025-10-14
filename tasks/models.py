# tasks/models.py
from django.db import models
from django.utils import timezone

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

class Task(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Other')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
    due_date = models.DateTimeField(null=True, blank=True)
    # ... other fields

class SubTask(models.Model):
    parent = models.ForeignKey(Task, related_name='subtasks', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Other')  # ✅ works now



    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Other')
    due_date = models.DateField(null=True, blank=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
    done = models.BooleanField(default=False)


    def is_overdue(self):
        if self.due_date and self.due_date < timezone.now().date() and not self.completed:
            return True
        return False

    def __str__(self):
        return self.title
