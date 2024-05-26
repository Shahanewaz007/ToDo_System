from django import forms
from .models import ToDoModel

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDoModel
        fields = ['taskTitle', 'taskDescription', 'priority', 'due_date']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'})
        }