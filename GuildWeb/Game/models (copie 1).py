from django.db import models

# Create your models here.

class Compte(models.Model):
	User = models.ForeignKey('User', on_delete=models.CASCADE,
	FACTION_IN_WORLD = (
		('RO', 'rouge'),
		('VE', 'vert'),
		('BL', 'bleu'),)
	faction_in_world = models.CharField(
		max_length=2,
		choices=FACTION_IN_WORLD,
		default='RO',)

	REGION_IN_WORLD = (
		('', ''),
		('', ''),
		('', ''),
		('', ''),)
	region_in_world = models.CharField(
		max_length=2,
		choices=REGION_IN_WORLD,
		default='',)

	feuille = models.IntegerField(default=0)
	goutte = models.IntegerField(default=0)
	cendres = models.IntegerField(default=0)
	talisman = models.IntegerField(default=0)








