from django.shortcuts import render, get_object_or_404 , redirect
from django.utils import timezone
from .models import Project
# Create your views here.

def home(request):
    projects=Project.objects
    return render(request, 'home.html', {'projects':projects})


def project_detail(request):
    return render(request, 'project_detail.html')



def center(request, project_id):
    project_center = get_object_or_404(Project, pk=project_id)
    return render(request, 'center.html', {'project': project_center})

def about(request):
    return render(request, 'about.html')





