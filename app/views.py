"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def jokes(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/jokes.html',
        {
            'title':'Joke API',
            'message':'API implementation page',
            'year':datetime.now().year,
        }
    )

def tellJoke(request1):
    from urllib import request
    import json

    #this is to request a joke from the API
    req = request.Request("https://official-joke-api.appspot.com/random_joke")

    #this converte the request object to a readable object
    text = request.urlopen(req)

    #this converts it to a JSON object
    text = text.read()

    #loading the JSON and printing it in the following lines
    jokeJson = json.loads(text)
    jokeString = (jokeJson['setup'] + " " + jokeJson['punchline'])

    return render(
        request1,
        'app/jokes.html',
        {
            'title':'Joke API',
            'message':'API Implementaion page',
            'year':datetime.now().year,
            'joke':jokeString
        }
        )
