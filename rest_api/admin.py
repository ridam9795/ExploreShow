from django.contrib import admin
from .models import Movie, Event,Sport,Activity
# Register your models here.
admin.site.register((Movie, Event, Sport, Activity))
