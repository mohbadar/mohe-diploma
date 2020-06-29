from django.shortcuts import render, get_object_or_404
from ..tenant.models import Tenant, Center , Template
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
# Create your views here.

@login_required
# @permission_required('*.*')
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


# def login_request(request):
#     form = AuthenticationForm()
#     return render(request=request, template_name="account/login.htlm", context={"form":form})


