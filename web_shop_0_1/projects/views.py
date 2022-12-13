from django.shortcuts import render
from django.views import generic

from web_shop_0_1.projects.models import Project


def show_projects(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'projects/projects.html', context)


class ProjectDetailsView(generic.DetailView):
    model = Project
    template_name = 'projects/project_details.html'
