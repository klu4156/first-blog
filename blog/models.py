from django.db import models

# Create your models here.
from django.utils import timezone

class Post(models.Model): #class defines object, post is model name
	author = models.ForeignKey('auth.User') #link to other model
	title = models.CharField(max_length=200) #text with limited number of characters
	text = models.TextField() #long text, no limit
	created_date = models.DateTimeField(
		default=timezone.now) #date and time
	published_date = models.DateTimeField(
		blank=True, null=True)
	
	def publish(self): #both methods belong to Post
		self.published_date = timezone.now()
		self.save()
	
	def __str__(self):
		return self.title