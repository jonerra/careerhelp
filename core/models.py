from django.db import models

# Create your models here.
class Contact(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField(max_length=200, blank=False, unique=False)
	message = models.TextField(max_length=500, null=True, blank=True)

	def __str__(self):
		return self.email

class Service(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True)
	slug = models.SlugField(max_length=100)
	price = models.DecimalField(max_digits=10, decimal_places=2)

	def __str__(self):
		return self.name