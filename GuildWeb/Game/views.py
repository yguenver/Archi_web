
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import redirect

from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Compte, Msg

from .forms import ConnexionForm, InscriptionForm, MessageForm


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
			print(user)
			if user is not None:
				login(request, user)  # nous connectons l'utilisateur
				return redirect(reverse(ConnexionView))
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
			name = form.cleaned_data["pseudo"]
			email = form.cleaned_data["email"]
			passw = form.cleaned_data["password"]
			passwordconf = form.cleaned_data["passwordconf"]
			if passw != passwordconf:
				error = True
			else:
				try:
					user = User.objects.create_user(name, email, passw)
				except:
					return render(request,'inscription.html', {'form' : form})
				
				if user is not None:
					user.save()
					useraccount = Compte.objects.create(user=user)
					useraccount.save()
					print(user)
					user = authenticate(username=name, password=passw)
					print(user)
					login(request, user)
					return redirect(reverse(ConnexionView))
				else:
					error = True
		else:
 			error = True
	else:
		form = InscriptionForm()

	return render(request,'inscription.html', {'form' : form})


	
def MsgView(request):

	if request.method == "POST":
		form = MessageForm(request.POST)
		if request.POST['mode'] == "Boite reception":
			try:
				recu = Msg.objects.get(receiver=request.user.username)
				print(recu)
			except:
				recu = None
			print(recu)
			return render(request, 'Messages.html', {'mode': "R"}, {'msgrecu': recu})
		if request.POST['mode'] == "Nouveau message":
			return render(request, 'Messages.html', {'mode': "S"}, {'form' : form})
		if request.POST['mode'] == "Envoyer":
			try:
				dest = User.objects.get(username=request.POST['destinataire'])
			except User.DoesNotExist:
				dest = None
			
			if dest != None:				
				print(dest)
				print(request.user)
				print(request.POST['objet'])
				print(request.POST['message'])
				msg = Msg.objects.create(sender=request.user.username, receiver=dest.username, objet=request.POST['objet'], text=request.POST['message'])
				msg.save()
				print (msg)
				return render(request, 'Messages.html', {'mode': "R"})
			else:
				try:
					recu = Msg.objects.get(receiver=request.user)
				except:
					recu = None
				return render(request, 'Messages.html', {'mode': "R"}, {'msgrecu': recu})
				#msg erreur destina
	else:
		try:
			recu = Msg.objects.get(receiver=request.user)
		except:
			recu = None
		return render(request, 'Messages.html', {'mode': "R"}, {'msgrecu': recu})

	
	

def ContactView(request):
	return render(request,'contact.html')

@login_required(login_url='/connexion')
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
