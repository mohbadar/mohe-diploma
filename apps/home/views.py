from django.shortcuts import render, get_object_or_404
from ..tenant.models import Tenant, Center , Template
from django.http import JsonResponse

# Create your views here.


def get_home(request):
    return render(request, "home/index.html")

def get_newform_view(request):
    tenants = Tenant.objects.all()
    return render(request, "home/newform.html", {'tenants': tenants})


def get_centers_of_tenant(request,code):
    # tenantCode = request.GET.dict()['code']

    centers = Center.objects.filter(tenant = Tenant.objects.filter(code=code).first())
    # centers = list(Center.objects.all().values())
    data = dict()
    data['centers'] = centers
    return JsonResponse(data)