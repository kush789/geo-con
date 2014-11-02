from django.db import models
from django.contrib.auth.models import User
from time import time

def get_upload_file_name(instance, filename):
	return "uploaded_file/%s_%s" % (str(time()).replace('.','_'), filename)

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	pub_date = models.DateTimeField('date published', blank=True, null=True)
	user = models.ForeignKey(User, null=True, blank=True)
	likes = models.IntegerField(default=0)
	thumbnail = models.FileField(upload_to=get_upload_file_name, blank=True, null=True)

	def __unicode__(self):
		return self.title

class Comment(models.Model):
	body = models.CharField(max_length=150)
	pub_date = models.DateTimeField('date published', blank=True, null=True)
	user = models.ForeignKey(User, null=True, blank=True) 	
	post = models.ForeignKey(Post, null=True, blank=True)
	pid = models.IntegerField(null=True, blank=True)
	uid = models.IntegerField(null=True, blank=True)
	likes = models.IntegerField(default=0)

	
	def __unicode__(self):
		return self.body
	

class Like(models.Model):
	post = models.ForeignKey(Post)
	user = models.ForeignKey(User)

class CLike(models.Model):
	comment = models.ForeignKey(Comment)
	user = models.ForeignKey(User)

class Follow(models.Model):
	fuser = models.ForeignKey(User, related_name='follower')
	fduser = models.ForeignKey(User, related_name='following')

class Stalk(models.Model):
	stalker = models.ForeignKey(User, related_name='stalker')
	stalked = models.ForeignKey(User, related_name='stalked')
	ctr =  models.IntegerField(default=1)





