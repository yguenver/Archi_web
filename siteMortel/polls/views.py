from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from django.shortcuts import get_object_or_404, render

from .models import Choice, Question



def accueil(request):	
	return render(request, 'polls/accueil.html')

def inscription(request):
	 return render(request, 'polls/inscription.html')


def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	template = loader.get_template('polls/index.html')
	context = {'latest_question_list':latest_question_list,}	
	return HttpResponse(template.render(context, request))

def detail(request, question_id):
	return HttpResponse("The question is... %s" % question_id)

def results(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {'question': question, 'error_message': "You didn't select a choice.", })
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


#return render(request, 'nom.html')
