from django.shortcuts import render, get_object_or_404

from reportlab.lib.units import mm
from reportlab.graphics.barcode import createBarcodeDrawing
from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics.charts.barcharts import HorizontalBarChart

from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from ..generic.models import Certificate, UserFacultyRelation


class BarcodeDrawing(Drawing):
    def __init__(self, text_value, *args, **kw):
        barcode = createBarcodeDrawing('Code128', value=text_value,  barHeight=10*mm, humanReadable=True)
        Drawing.__init__(self,barcode.width,barcode.height,*args,**kw)       
        self.add(barcode, name='barcode')

# Create your views here.

def barcode(request):
    d = BarcodeDrawing("kpu-10032")
    binaryStuff = d.asString('gif')
    return HttpResponse(binaryStuff, 'image/gif')

@login_required
# @permission_required('*.*')
def get_home(request):
    print("Profile", request.user)
    # item = UserFacultyRelation.objects.get(user = request.user.id).last()
    # certificates = Certificate.objects.filter(faculty=item.faculty.id)
    certificates = {}
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


