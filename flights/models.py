from django.db import models

# Create your models here.

""" MODELS are going to be a way of creating any 
python CLASS that is going to represent DATA that i want Django to STORE inside of a DATABASE. 
So when create a model, Django is going to figure out what SQL syntax 
it needs to use it to create or manipulate that SQL table. 
Selecting and updating and inserting anytime i make changes to those models.

For this particular app, 'Flight' class is going to inherit from models.model, that is going to be a model.
Then need to provide inside of this class all of the parameters that a flight has 
that I might want to keep track of (origin, destination, and duration).
Also, any model can implement '__str__' function, which returns a formated f string representation
of that particular object (this applies not just to Django models but to Python classes more generally).

For this app also create a class called 'Airport', that is also a model 
with parameteres (a 'code' for the airports code, as well as a 'city')
And also give this airport a string representation with '__str__' function. """


class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"

""" 'ForeignKey' references another table, in this case relationship between Flights and Airport tables. 
Give to 'origin' and 'destination' attributes a 'related_name', meaning if I have a Flight, 
I can use this attribute to access all of the Airports. And likewise, if I have an Airport, 
I can use this "origin & destinatios related_names" to access all of the Flights related to that Airport."""
class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"

""" add class 'Passengers' as a new Model, to the flights, to be able to represent 'Passengers' that might actually
be on these flights.  
Passengers properties; first name, last name, and flights as a 'many to many' relationship with flights 
that means a flight could have multiple passengers, and a passenger could be on multiple flights. 
Give to this 'flights' attribute a 'related_name' call "passengers", meaning if I have a passenger, 
I can use the flights attribute to access all of their flights. And likewise, if I have a flight, 
I can use this "passenger's related_name" to access all of the passengers who are on that flight. """


class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.first} {self.last}"



""" once the Django models classes are created with all the properties the class has,
next step is to tell Django to UPDATE changes to the database to include information about the models that have just created. 
This is a process called 'MIGRATIONS'.
It's a 2-step process;
1. Create a migration to say, there are some changes to apply to the database. We can make the migrations via command 'python manage.py makemigrations' 
2. Then Migrate them to tell Django to take those changes and actually apply them to the database. Via command 'python manage.py migrate'   """