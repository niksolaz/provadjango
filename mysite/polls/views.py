from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Question, Choice
from django.db.models import Sum, F
from django.views import generic

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"
    
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
    question = get_object_or_404(Question, pk=question_id)
    choice = Choice.objects.filter(question_id=question_id)
    total_votes = choice.aggregate(Sum('votes'))
    template = 'polls/results.html'
    context = {
        'question_id': question_id,
        'total_votes': total_votes,
        'choice': choice,
        'question': question
    }
    return render(request, template, context)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))