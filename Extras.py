import requests
import json
from Config import bcolors


def get_dad_joke():
    url = 'https://icanhazdadjoke.com/slack'
    response = requests.get(url)
    response = response.text
    data = json.loads(response)
    data = data['attachments']
    Joke = data[0]["text"]
    Joke = Joke.strip("\n").strip("\r")
    Joke = f"{bcolors.BOLD}{bcolors.OKBLUE}{Joke}{bcolors.ENDC}"
    return Joke
