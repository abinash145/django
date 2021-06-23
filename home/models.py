from django.db import models

# Create your models here.
class Contact(models.Model):
	name = models.CharField(max_length = 300)
	email = models.CharField(max_length = 300)
	subject = models.TextField()
	message = models.TextField()

	def __str__(self):
		return self.name


class Feedback(models.Model):
	name =models.CharField(max_length=400)
	post = models.CharField(max_length=400)
	comment = models.TextField()
	image = models.TextField()

	def __str__(self):
		return self.name
