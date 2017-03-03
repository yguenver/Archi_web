from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse


def index(request):
	return render(request,'index.html')
    #return HttpResponse("Hello, world. You're at the Game index.")