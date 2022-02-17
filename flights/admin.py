from django.contrib import admin

from .models import Flight, Airport, Passenger

# Register your models here.

""" This file 'admin.py' is a django pre-built app to be able to manipulate the Models (superuser admin)"""

""" (by defining the class 'FlightAdmin' for this particular app (or whatever class name) the /amdin interface may be customize,
in this particular case to display "id", "origin", "destination", "duration" data) """
class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")

""" also can define a class 'PassengerAdmin' for this particular app (or whatever class name) so when editing a passenger,
can have a special way of manipulating many to many relationships inside of an attribute called 'filter_horizontal', 
and if use a horizontal filter on flights, this will just make it a little bit nicer for manipulating
the flights that a passenger is on """

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)


admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, PassengerAdmin)
