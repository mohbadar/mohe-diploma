from django.shortcuts import render
from .models import Contact

from django.http.request import HttpRequest

# Create your views here.


def contact_savenew(request):

    if request.method == 'POST':
        print(request.POST.fromkeys("name"))
    return render(request, "home/index.html")
