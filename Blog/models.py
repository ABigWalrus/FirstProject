from django.db import models

class User(models.Model):
	name	= models.CharField(max_length=20)
	surname	= models.CharField(max_length=30)
	nickname= models.CharField(max_length=15)
	email	= models.EmailField(max_length=30)
	password= models.CharField(max_length=20)

