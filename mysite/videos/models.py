from django.db import models
from django.db.models.signals import pre_save
# Create your models here.

class Video(models.Model):
	date = models.DateTimeField()
	title = models.CharField(max_length = 200)
	description = models.CharField(max_length = 5000)
	video = models.URLField(max_length = 1000)
	creator = models.CharField(max_length=250)

	def __str__(self):
		return self.title + ": " + self.creator



class Article(models.Model):
	video = models.ForeignKey(Video, on_delete=models.CASCADE)
	context = models.TextField()
	##slug =  models.SlugField(unique=True)


	def __str__(self):
		print(self.video)
		return str(self.video)
