from django.contrib.auth import authenticate, login, logout
from audioop import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponseBadRequest
from django.urls import reverse



# Create your views here.

""" the 'Index' function it's going to display information about the currently signed in user,
signed into this website, and then presented with the index page. 
The view.index is going to check first if the user who tries to access this page is NOT authenticated,
this is checked by 'if not request.user.is_authenticated'
(the 'request' object that gets passed in as part of the request to every user in Django
automatically has a 'user' attribute associated with it,
and that user object has an 'is_authenticated' attribute that tells if the user is signed in or not.)
If the user is not signed in, go ahead and "return HttpResponseRedirect" him to the 'login view'.  
If the user do successfully logged in, then is going to be taken from '/login.html' to this 'index route',
wich will return render a template called 'users/user.html',
and inside of 'user.html', will display some information about the user who just logged in"""

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "users/user.html")

""" So if the user is NOT authenticated, then the app is going to redirect him to the "log in view", 
wich let's go ahead and render 'users/login.html', 
'login.html' is a Form where the user can log themselves in. 
The processing of the login data in 'login_view' as follows; the "login view function" could be called via 'POST' method, 
when user submit data to the log in form. Then first get the 'username=' which will be inside of the post data in a field called "username".
Also gets the 'password=', which will be in a field in the request.post inside of "password".
Then need to try to Authenticate the user; it is possible importing a couple of pre-built functions that Django has 
('from django.contrib.auth', and import three functions; one is 'authenticate' that checks if user name and password are correct,
other is called 'login', other is called 'logout').
After gotten the username and password, need to authenticate the user; check "if the user name and password are correct" ("user=authenticate.request.username password"),
Authenticate is a function wich just takes the request, takes a 'username', takes a 'password' and IF the username and password are valid,
gives back who the user actually is. And as long as the "user is not none", that means the authentication was successful, 
and go ahead and log the user in, using a pre-built function Django has "Logging in".
And so that's if the user is not none, meaning if the authentication was successful, go ahead and 'redirect via HttpResponseRedirect' the user back to the index route back 
to the original route that the user started out.
But otherwise, if the authentication failed, go ahead and render the same users login page again, 
but with some additional context; display a "message" that says 'invalid credentials'.
(this message logic will be inside of a div in 'login.html', so if there is a message, the user see the message printed.
Otherwise, won't see it at all. """



def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "users/login.html", {
                "message": "Invalid credential, please try again."
            })


    return render(request, "users/login.html")

""" The way to log the user out is by using the Django "log out function" 
that handles log out logic instead of coding it.
So the 'logout_view' needs to make a call to this 'logout function'
and then, figure out where should the user go after they've been logged out.
taking them back to the "/login.html" page with a 'message' of logged out 
to indicate that the user has now been logged out."""

def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {
        "message": "your are now Logged out."
    })
