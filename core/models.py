from django.db import models

# Create your models here.
class Contact(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField(max_length=200, blank=False, unique=False)
	message = models.TextField(max_length=500, null=True, blank=True)

	def __str__(self):
		return self.email