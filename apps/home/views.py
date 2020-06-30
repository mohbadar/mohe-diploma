from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from ..generic.models import Certificate, UserFacultyRelation
# Create your views here.

@login_required
# @permission_required('*.*')
def get_home(request):
    print("Profile", request.user)
    userFacultyRelation = UserFacultyRelation.objects.get(user = request.user.id)
    certificates = Certificate.objects.filter(faculty=userFacultyRelation.faculty.id)
    return render(request, "home/index.html", {"certificates": certificates})

def get_newform_view(request):
    # tenants = Tenant.objects.all()
    tenants = ()
    return render(request, "home/newform.html", {'tenants': tenants})


def get_centers_of_tenant(request,code):
    # tenantCode = request.GET.dict()['code']

    centers = ()
    # centers = list(Center.objects.all().values())
    data = dict()
    data['centers'] = centers
    return JsonResponse(data)


# def login_request(request):
#     form = AuthenticationForm()
#     return render(request=request, template_name="account/login.htlm", context={"form":form})


