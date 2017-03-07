from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
	#ex: /polls/accueil/
	url('accueil/', views.accueil, name='accueil'),
	#ex: /polls/inscription/
	url('inscription/', views.inscription, name='inscription'),


	# ex: /polls/
	url(r'^$', views.index, name='index'),
	# ex: /polls/3
	url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
	# ex: /polls/3/results/
	url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
	# ex: /polls/3/vote
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]



#return render(request, 'nom.html')
