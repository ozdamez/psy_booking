from django.contrib import admin
from .models import Person, Visit, Place, Booking
# Register your models here.
admin.site.register(Person)
admin.site.register(Place)
admin.site.register(Visit)
admin.site.register(Booking)