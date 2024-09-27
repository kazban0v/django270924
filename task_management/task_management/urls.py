from django.contrib import admin
from django.urls import path, include
from tasks.views import TaskListView  
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),  
    path('users/', include('users.urls')),  
    path('', TaskListView.as_view(), name='home'),  
    path('', include('django.contrib.auth.urls')),  
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
]
