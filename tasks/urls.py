from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_task/', views.add_task, name='add_task'),
    path('toggle_done/<int:task_id>/', views.toggle_done, name='toggle_done'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
]
