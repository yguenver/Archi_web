from django.conf.urls import url
from django.contrib import admin

from . import views


urlpatterns = [
	url(r'^connexion', views.ConnexionView, name='connexion'),
	url(r'^inscription', views.InscriptionView, name='inscription'),
	url(r'^deconnexion', views.deconnexion, name='deconnexion'),
	url(r'^1', views.ProfilView, name='profil'),
	url(r'^base', views.BaseView, name='base'),
	url(r'^chat', views.ChatView, name='chat'),
	url(r'^amis', views.AmisView, name='amis'),
	url(r'^evenement', views.EvenementView, name='evenement'),
]
