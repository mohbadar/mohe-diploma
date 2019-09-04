from django.shortcuts import render
from apps.post import models
# Create your views here.


def get_home(request):
    posts = models.Post.objects.all().order_by('-created_at')[:3]   
    return render(request, "home/index.html",{'posts':posts})