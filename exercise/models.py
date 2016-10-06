from django.db import models

class Exercise(models.Model):
	name			=models.CharField(max_length=200,unique=True)
	title			=models.CharField(max_length=200)
	description		=models.TextField(null=True,blank=True)
	instruction		=models.TextField()
	image			=models.ImageField(upload_to="exercise/images")
	audio			=models.CharField(max_length=100)
	video			=models.URLField()

	def __unicode__(self):
		return self.title



class Workout(models.Model):
	name				=models.CharField(max_length=200,unique=True)
	title				=models.CharField(max_length=200)
	exercise			=models.ForeignKey(Exercise)
	duration			=models.DateTimeField()
	rest_duration		=models.DateTimeField()

	def __unicode__(self):
		return self.title	







