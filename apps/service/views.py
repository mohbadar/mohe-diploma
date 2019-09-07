from django.shortcuts import render, get_object_or_404
from .models import Service, ServiceCateory
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def get_service(request, slug):
    service = get_object_or_404(Service, slug=slug)
    
    return render(request, 'service/show.html', {
        "service":service
    })


def get_service_categories(request):

    service_categories = list(ServiceCateory.objects.all().values())
    data = dict()
    data['service_categories'] = service_categories

    return JsonResponse(data)

def get_services_of_category(request, name):
	services = Service.objects.filter(category = ServiceCateory.objects.filter(name=name).first())
	page = request.GET.get('page',6)

	paginator = Paginator(services,6)

	try:
		services = paginator.page(page)
	except PageNotAnInteger:
		services = paginator.page(1)
	except EmptyPage:
		services = paginator.page(paginator.num_pages)

	return render(request, "service/services.html", {'services':services})


def get_all_services(request):
	services = Service.objects.all()
	page = request.GET.get('page',6)

	paginator = Paginator(services,6)

	try:
		services = paginator.page(page)
	except PageNotAnInteger:
		services = paginator.page(1)
	except EmptyPage:
		services = paginator.page(paginator.num_pages)

	return render(request, "service/services.html", {'services':services})