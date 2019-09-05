from django.shortcuts import render, get_object_or_404
from .models import Page, PageCategory
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def get_page(request, slug):
    page = get_object_or_404(Page, slug=slug)
    
    return render(request, 'page/show.html', {
        "page":page
    })


def get_page_categories(request):

    page_categories = list(PageCategory.objects.all().values())
    data = dict()
    data['page_categories'] = page_categories
    return JsonResponse(data)

def get_pages_of_category(request, name):
	pages = Page.objects.filter(category = PageCategory.objects.filter(name=name).first())
	page = request.GET.get('page',6)

	paginator = Paginator(pages,6)

	try:
		pages = paginator.page(page)
	except PageNotAnInteger:
		pages = paginator.page(1)
	except EmptyPage:
		pages = paginator.page(paginator.num_pages)

	return render(request, "page/pages.html", {'pages':pages})