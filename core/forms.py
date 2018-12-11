from django import forms
from core.models import Contact

class ContactForm(forms.ModelForm):
	first_name = forms.CharField(
		max_length=Contact._meta.get_field('first_name').max_length,
		help_text="First Name: "
	)
	last_name = forms.CharField(
		max_length=Contact._meta.get_field('last_name').max_length,
		help_text="Last Name: "
	)
	subject = forms.CharField(
		max_length=Contact._meta.get_field('subject').max_length,
		help_text="Subject: "
	)
	message = forms.CharField(
		max_length=Contact._meta.get_field('message').max_length,
		help_text="Message: "
	)

	class Meta:
		model = Contact
		fields = ('first_name', 'last_name', 'subject', 'message')