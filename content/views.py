from django.shortcuts import render, redirect
from .models import Project
from django.views.generic import ListView, CreateView
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import ProjectForm


# Create your views here.
def project_list_view(request):
    projects = Project.objects.all()
    
    return render(request, 'content/project_list.html', {'projects': projects})

from django.shortcuts import render, redirect
from .forms import ProjectForm

# def add_project_view(request):
#     form = ProjectForm()
#     return render(request, 'content/add_project.html', {'form': form})

def add_project_view(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project added successfully!')
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'content/add_project.html', {'form': form})
    

