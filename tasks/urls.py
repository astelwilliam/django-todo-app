from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='index'),
    path('add_task/', views.add_task, name='add_task'),
    path('toggle_done/<int:task_id>/', views.toggle_done, name='toggle_done'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('share/<int:task_id>/', views.share_task, name='share_task'),
    path('accounts/', include('django.contrib.auth.urls')),  # login/logout
    path('signup/', views.signup, name='signup'),
]
