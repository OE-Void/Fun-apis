import requests
import json

m = requests.get("http://127.0.0.1:8000/insult/api")
l = requests.get("http://127.0.0.1:8000/joke/api")

print("Insult:", m.text) 
print("Joke:", l.json())