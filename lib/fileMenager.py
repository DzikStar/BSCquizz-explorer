import requests
import os
import json

def downloadTexts(lang):

    url = 'https://event.brawlstars.com/assets/events/cards/'+lang+'.json'
    filename_01 = 'texts.json'

    req = requests.get(url, 'html.parser')

    with open(filename_01, 'w', encoding="utf8") as file:
        file.write(req.text)
        file.close()
    
    os.system('move texts.json webCache/ && cls')

    with open('webCache\\texts.json', 'r+', encoding="utf8") as file:
        fData = json.load(file)
        file.seek(0)
        json.dump(fData, file, indent=4)
        