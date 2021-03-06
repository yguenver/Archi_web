import datetime
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Compte(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	FACTION_IN_WORLD = (
		('RO', 'rouge'),
		('VE', 'vert'),
		('BL', 'bleu'),
		('NA', 'neutral'),)
	faction_in_world = models.CharField(
		max_length=2,
		choices=FACTION_IN_WORLD,
		default='NA',)

	REGION_IN_WORLD = (
		('KT', 'kato'),
		('JT', 'joto'),
		('HN', 'hone'),
		('SN', 'sino'),)
	region_in_world = models.CharField(
		max_length=2,
		choices=REGION_IN_WORLD,
		default='KT',)

	feuille = models.IntegerField(default=0)
	goutte = models.IntegerField(default=0)
	cendres = models.IntegerField(default=0)
	talisman = models.IntegerField(default=0)
	

class Msg(models.Model):
	sender = models.CharField(max_length=50, default="error sender")
	receiver = models.CharField(max_length=50, default="error receiver")
	objet = models.CharField(max_length=50, default="No object")
	text = models.CharField(max_length=255, default="No text")
	date = models.DateField(default=datetime.now())
