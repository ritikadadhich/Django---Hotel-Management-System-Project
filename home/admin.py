from django.contrib import admin
from home.models import Contact
from .models import Room, Booking
# Register your models here.
admin.site.register(Contact)
admin.site.register(Room)
admin.site.register(Booking)