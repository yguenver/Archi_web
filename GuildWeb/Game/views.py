from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.core import serializers
from django.contrib.auth.models import User
from .models import Compte
import json




def GameView(request):
	#json_user = serializers.get_serializer("json", User.objects.all())
	#user = json_serializer.serialize(user.objects.all().order_by('id')[:5], ensure_ascii=False)

	usr = User.objects.get(username="user1")
	#Compte.objects.create(user=usr)
	cpt = Compte.objects.get(user=usr)
	print (usr.username)
	print (cpt.region_in_world)
	print(usr)

	#current_user_id = request.user.id
	#context['current_user_id'] = current_user_id
	return render(request, 'index.html', {'user': usr, 'compte': cpt})
    #return HttpResponse("Hello, world. You're at the Game index.")
