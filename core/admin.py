from django.contrib import admin
from core.models import Contact, Service

# Register your models here.
admin.site.register(Contact)

class ServiceAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}

admin.site.register(Service, ServiceAdmin)