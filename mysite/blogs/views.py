from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the blogs index.")

def detail(request, blog_id):
    return HttpResponse("You're looking at blog %s." % blog_id)

