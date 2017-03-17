from django.contrib.auth import authenticate, login, logout
from django.views import generic
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

from .models import *
from .forms import *


def AccueilView(request):
	return render(request,'accueil.html')
	
def GameView(request):
	return render(request,'game.html')

def ConnexionView(request):
	error = False
    
	if request.method == "POST":
		form = ConnexionForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data["username"]
			passw = form.cleaned_data["password"]
			user = authenticate(username=name, password=passw)  # Nous vérifions si les données sont correctes
			if user is not None:
				login(request, user)  # nous connectons l'utilisateur
				return redirect(reverse(ProfilView))
			else: # sinon une erreur sera affichée
				error = True
	else:
		form = ConnexionForm()
	return render(request, 'connexion.html', {'form' : form})


def InscriptionView(request):
	error = False

	if request.method == "POST":
		form = InscriptionForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data["pseudo"]
			#name = form.cleaned_data["prenom"]
			#lastname = form.cleaned_data["nom"]
			email = form.cleaned_data["email"]
			password = form.cleaned_data["password"]
			passwordconf = form.cleaned_data["passwordconf"]
			if password != passwordconf:
				error = True
			else:
				user = User.objects.create_user(username, email, password)
				#user.first_name, user.last_name = name, lastname
				if user:
					login(request, user)
				else:
					error = True
		else:
 			error = True
	else:
		form = InscriptionForm()

	return render(request,'inscription.html', locals())


def ContactView(request):
	return render(request,'contact.html')

@login_required(login_url='/connexion/')
def ProfilView(request):
	return render(request,'profil.html')

def deconnexion(request):
	logout(request)
	return redirect(reverse(ConnexionView))

@login_required
def AmisView(request):
	return render(request,'amis.html')

@login_required
def EvenementView(request):
	return render(request,'evenement.html')

@login_required
def ChatView(request):
	return render(request,'chat.html')

@login_required
def BaseView(request):
	return render(request,'base.html')

# Create your views here.
