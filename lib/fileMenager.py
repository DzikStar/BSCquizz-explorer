import requests
import os
import json

def download():
    
    url = 'https://event.brawlstars.com/assets/events/cards/en.json'
    filename_01 = 'texts.json'

    req = requests.get(url, 'html.parser')

    with open(filename_01, 'w') as file:
        file.write(req.text)
        file.close()
    
    os.system('move texts.json webCache/ && cls')