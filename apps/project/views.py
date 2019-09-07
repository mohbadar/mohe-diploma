from django.shortcuts import render, get_object_or_404
from .models import Project, ProjectCategory
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def get_project(request, slug):
    project = get_object_or_404(Project, slug=slug)
    
    return render(request, 'project/show.html', {
        "project":project
    })


def get_project_categories(request):

    project_categories = list(ProjectCategory.objects.all().values())
    data = dict()
    data['project_categories'] = project_categories

    return JsonResponse(data)

def get_projects_of_category(request, name):
	projects = Project.objects.filter(category = ProjectCategory.objects.filter(name=name).first())
	page = request.GET.get('page',6)

	paginator = Paginator(projects,6)

	try:
		projects = paginator.page(page)
	except PageNotAnInteger:
		projects = paginator.page(1)
	except EmptyPage:
		projects = paginator.page(paginator.num_pages)

	return render(request, "project/projects.html", {'projects':projects})



def get_all_projects(request):
	projects = Project.objects.all()
	page = request.GET.get('page',6)

	paginator = Paginator(projects,6)

	try:
		projects = paginator.page(page)
	except PageNotAnInteger:
		projects = paginator.page(1)
	except EmptyPage:
		projects = paginator.page(paginator.num_pages)

	return render(request, "project/projects.html", {'projects':projects})