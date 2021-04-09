from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	ip =  models.CharField(max_length=15)


class Message(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	content = models.CharField(max_length=100)
	time = models.DateTimeField(auto_now=True)