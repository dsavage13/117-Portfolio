from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'year', 'image', 'repository', 'skill']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Project Title'}),
            'description': forms.Textarea(attrs={'placeholder': 'Project Description'}),
            'year': forms.NumberInput(attrs={'placeholder': 'Project Year'}),
            'image': forms.ClearableFileInput(attrs={'placeholder': 'Project Image'}),
            'repository': forms.URLInput(attrs={'placeholder': 'Project Repository'}),
            'skill': forms.CheckboxSelectMultiple(),
        }
        


