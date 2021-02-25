def tellMeJokes():
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
    return (jokeJson['setup'] +"\n" + jokeJson['punchline'])