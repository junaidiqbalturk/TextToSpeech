import requests  #The Standard module for requesting from web
import json      #The JSON Module
import pyttsx3   #Python Text to Speech Module
from joke import Joke

url = "https://official-joke-api.appspot.com/random_ten" #API URL for Jokes


response= requests.get(url)
print(response.status_code)

jsonData = json.loads(response.text)

#Intializing Array Object
jokes = []

for j in jsonData:
    setup = j["setup"]
    punchline = j["punchline"]
    joke = Joke(setup,punchline)
    jokes.append(joke)

print(f"Got {len(jokes)} jokes")

for joke in jokes:
    # print(joke)
    pyttsx3.speak("setup")
    pyttsx3.speak(joke.setup)
    pyttsx3.speak("The Punch Line")
    pyttsx3.speak(joke.punchline)