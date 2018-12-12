from django import forms
from core.models import Contact

class ContactForm(forms.ModelForm):
	name = forms.CharField(
		max_length=Contact._meta.get_field('name').max_length,
		help_text="Name: "
	)
	email = forms.CharField(
		max_length=Contact._meta.get_field('email').max_length,
		help_text="Email: "
	)
	message = forms.CharField(
		max_length=Contact._meta.get_field('message').max_length,
		help_text="Message: "
	)

	class Meta:
		model = Contact
		fields = ('name', 'email', 'message')