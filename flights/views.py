from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

import flights

from .models import Flight, Passenger


# Create your views here.


def index(request):
    return render(request, "flights/index.html",{
        "flights": Flight.objects.all()
    })

""" On the flight.html page, display information about Flights and which passengers
happened to be on any given flight.
("non_passengers" variable is defined (by '.exclude' method) for showing people that are NOT already on a flight 
and can be selected from a list in the Book Form via flight.html   """

def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id) #'pk' = primary key
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passenger": Passenger.objects.exclude(flights=flight)
    })

""" in addition to displaying all the passengers on any particular flight,
the app also gives the ability to "add passengers to a flight" via '/book' url and 'view.book' that takes as arguments 'request' but also 'flight_id'.
Inside of urls.py the path "int:flight_id/book" is going to let the user book a flight for this particular 'flight_ID' 
(for flight one or flight two or flight three, or so forth...).
This 'view.book' y going to check when this book route is called upon, this means If request method is POST, 
then define 'flight' var as an object that get the flight whose primary key (pk) is that 'flight_ID',
and then, associate with the form, When the user submits the form to book a new passenger on the flight,
should tell what the ID of the passenger is, What passenger should the app book on the flight 
(those are the two pieces of information needed to know in order to actually book a flight; the flight and the passenger information.

The passenger information is going to be in a 'request.post' and ["passenger"] attribute.
This means that the data about which passenger ID the user want to register on this flight is going
to be passed in via a form with an input field name 'passenger' 
(by default this might be a string, so need to convert it into an 'integer' just to make sure dealing with an integer ID).

So in summary, if the request method is post, meaning some User submitted the book form via the post request method,
the view is going to get a particular flight via 'flights.objects.get', get the flight with that 'flight_ID'.
And then, getting a passenger, which passenger? the one who's pk (their primary key, otherwise known as ID)
is equal to whatever was submitted via this post form with a name of 'passenger'.
Finally, this view is going to add a new row into a table taht keeps track the passengers flights, 
via 'passenger.flights.add(flight)', and when all this is done, the user is return back to the flight url page via 'response HttpResponseRedirect' .   """

def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight", args=(flight_id,)))
