from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Question, Choice
from django.db.models import Sum

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = 'polls/index.html' # load this template
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, template, context) # render the template with the context

def about(request):
    return HttpResponse("This is the about page.")

def detail(request, question_id):
    try:
        question = get_object_or_404(Question, pk=question_id)
        template = 'polls/detail.html'
        context = {
            'question': question,
        }
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, template, context)

def results(request, question_id):
    choice = Choice.objects.filter(question_id=question_id)
    total_votes = choice.aggregate(Sum('votes'))
    template = 'polls/results.html'
    context = {
        'question_id': question_id,
        'total_votes': total_votes,
    }
    return render(request, template, context)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)