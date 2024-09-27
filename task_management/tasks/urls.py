from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='task-list'),
    path('task/new/', views.TaskCreateView.as_view(), name='task-create'),
    path('task/<int:pk>/edit/', views.TaskUpdateView.as_view(), name='task-update'),
    path('task/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task-delete'),
    path('task/<int:pk>/comment/', views.add_comment, name='task-comment'),  
]
