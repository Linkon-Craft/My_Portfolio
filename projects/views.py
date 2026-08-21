from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm



def home(request):
    all_projects = Project.objects.all()
    return render(request, 'project/home.html', {"all_projects":all_projects})

def project_list(request):
    all_projects = Project.objects.all()
    return render(request, 'project/projects.html', {"all_projects":all_projects})

def project_detail(request, pk):

    project = get_object_or_404(
        Project,
        pk=pk
    )

    return render(request, "project/project_detail.html", {"project": project})


def add_project(request):
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('projects:home')
    return render(request, 'project/add_project.html', {"form":form})  


