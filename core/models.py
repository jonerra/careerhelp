from django.db import models

# Create your models here.
class Contact(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	subject = models.CharField(max_length=250)
	message = models.CharField(max_length=500)

	def __str__(self):
		return self.subject