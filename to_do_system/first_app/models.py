from django.db import models


class ToDoModel(models.Model):
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]
    taskTitle = models.CharField(max_length=30)
    taskDescription = models.TextField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Low')
    due_date = models.DateField(null=True, blank=True)
    is_complete = models.BooleanField(default=False)
    
    def __str__(self):
        return self.taskTitle

