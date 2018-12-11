from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from core.forms import ContactForm

# Create your views here.
class Home(TemplateView):
	template_name = "home.html"

def index(request):
	context_dict = {'boldmessage': "Hello Word"}
	return render(request, 'careerhelp/index.html', context=context_dict)

def contact_us(request):
	form = ContactForm()

	if request.method == 'POST':
		form = ContactForm(request.POST)

		if form.is_valid():
			form.save(commit=True)
			return index(request)
	else:
		print(form.errors)

	return render(request, 'careerhelp/contact.html', {'form': form})