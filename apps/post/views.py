from django.shortcuts import render, get_object_or_404
from .models import Post, PostCateory
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def get_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    
    return render(request, 'post/show.html', {
        "post":post
    })


def get_post_categories(request):

    post_categories = list(PostCateory.objects.all().values())
    data = dict()

    data['post_categories'] = post_categories

    return JsonResponse(data)

def get_posts_of_category(request, name):
	posts = Post.objects.filter(category = PostCateory.objects.filter(name=name).first())
	page = request.GET.get('page',6)

	paginator = Paginator(posts,6)

	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	return render(request, "post/posts.html", {'posts':posts})