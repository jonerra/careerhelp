from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView
from core.forms import ContactForm
from core.models import Service

# Create your views here.
class Home(TemplateView):
	template_name = "home.html"

# def index(request):
# 	context_dict = {'boldmessage': "Hello Word"}
# 	return render(request, 'careerhelp/index.html', context=context_dict)

def index(request):
	form = ContactForm()

	if request.method == 'POST':
		form = ContactForm(request.POST)

		if form.is_valid():
			form.save(commit=True)
			# return index(request)
	else:
		print(form.errors)

	return render(request, 'careerhelp/index.html', {'form': form})

def service_detail(request, slug):
	service = get_object_or_404(Service, slug=slug)
	context = {
		'service': service
	}
	return render(request, 'careerhelp/service_detail.html', context)
