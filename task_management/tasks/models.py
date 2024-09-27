from django.db import models
from django.contrib.auth.models import User
from datetime import date  

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField(default=date.today)  
    priority = models.CharField(max_length=10, choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')])
    status = models.CharField(max_length=10, choices=[('completed', 'Completed'), ('incomplete', 'Incomplete')])
    assigned_to = models.ForeignKey(User, related_name='tasks', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title



class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.task}'
