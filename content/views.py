from django.shortcuts import render
from .models import Project

# Create your views here.
def project_list_view(request):
    projects = Project.objects.all()
    
    return render(request, 'content/project_list.html', {'projects': projects})


