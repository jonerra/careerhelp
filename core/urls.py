from django.urls import path
from core import views

urlpatterns = [
	path('', views.index, name='index'),
	path('services/<slug>/', views.service_detail, name='service_detail'),
]