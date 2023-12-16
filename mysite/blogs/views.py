from django.http import Http404
from django.shortcuts import get_object_or_404, render
from .models import Blog
from django.urls import reverse

# Create your views here.
def index(request):
    list_blog = Blog.objects.all()
    template = 'blogs/index.html'
    context = {
        'list_blog': list_blog
    }
    return render(request, template, context)
    

def detail(request, blog_id):
    try:
        blog = get_object_or_404(Blog, pk=blog_id)
        template = 'blogs/detail.html'
        context = {
            'blog': blog,
        }
    except Blog.DoesNotExist:
        raise Http404("Blog does not exist")
    return render(request, template, context)

