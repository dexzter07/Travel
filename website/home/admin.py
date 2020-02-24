from django.contrib import admin
from . models import Destinations, Contact, Inquiry, Package
# Register your models here.

admin.site.register(Destinations)
admin.site.register(Contact)
admin.site.register(Inquiry)
admin.site.register(Package)
