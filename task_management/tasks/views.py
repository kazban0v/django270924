from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User, Group
from .models import Task, Comment 
from .forms import TaskForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    login_url = 'login'

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.GET.get('assigned_to_me'):
            queryset = queryset.filter(assigned_to=self.request.user)
        if self.request.user.groups.filter(name='Project Manager').exists():
            pass
        else:
            queryset = queryset.filter(assigned_to=self.request.user)
        
       
        if self.request.GET.get('status'):
            queryset = queryset.filter(status=self.request.GET.get('status'))
        if self.request.GET.get('date_sort') == 'asc':
            queryset = queryset.order_by('due_date')
        elif self.request.GET.get('date_sort') == 'desc':
            queryset = queryset.order_by('-due_date')
        if self.request.GET.get('priority'):
            queryset = queryset.filter(priority=self.request.GET.get('priority'))
        
        return queryset


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'tasks/task_form.html'
    form_class = TaskForm

    def form_valid(self, form):
        task = form.save(commit=False)
        if not self.request.user.groups.filter(name='Project Manager').exists():
            task.assigned_to = self.request.user
        task.save()
        return redirect('task-list')


class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    template_name = 'tasks/task_form.html'
    form_class = TaskForm

    def test_func(self):
        task = self.get_object()
        if self.request.user.groups.filter(name='Project Manager').exists():
            return True
        return task.assigned_to == self.request.user

    def form_valid(self, form):
        task = form.save(commit=False)
        if not self.request.user.groups.filter(name='Project Manager').exists():
            task.assigned_to = self.request.user
        task.save()
        return redirect('task-list')


class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('task-list')

    def test_func(self):
        task = self.get_object()
        if self.request.user.groups.filter(name='Project Manager').exists():
            return True
        return task.assigned_to == self.request.user

def add_comment(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        text = request.POST.get('text')
        Comment.objects.create(task=task, author=request.user, text=text)
        return redirect('task-detail', pk=pk)
    return HttpResponseForbidden()
