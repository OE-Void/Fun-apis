import random
import json
from fastapi import FastAPI
from roast import Roast

app = FastAPI(
  title = "Fun - APIs",
  description = "Get access to hundresds of fun apis to host locally and use them at a single endpoint"
)

with open("jokes.json", "r") as f:
  jokes = json.load(f)

@app.get("/insult/api")
def rost():
  m = Roast()
  return m.get_punchline()

@app.get('/joke/api')
def send_joke():
    return random.choice(jokes)
