from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from . import views

app_name = 'Game'
urlpatterns = [

	#ex: /Game/
	url(r'^GamePage/', views.GameView, name='index'),
]