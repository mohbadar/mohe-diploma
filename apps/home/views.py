from django.shortcuts import render
# Create your views here.


def get_home(request):
    return render(request, "home/index.html")

def get_newform_view(request):
    return render(request, "home/newform.html")