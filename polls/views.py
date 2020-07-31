from django.http import HttpResponse
from .models import Question

def index(request):
    """show the last 5 question entries
    Request: polls/
    """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def detail(request, question_id):
    """show details of a question by its id
    Request: polls/15
    """

    return HttpResponse("aqui fica a questão %s." % question_id)

def results(request, question_id):
    """show vote results of a question
    Request: polls/15/results
    """

    response = "aqui fica os resultados da questão %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    """vote a question by its id

    Request:
        polls/15/vote
    """

    return HttpResponse("voce esta votando na questão %s" % question_id)