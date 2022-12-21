# ##############################################
# ####      Tool created by LeakBrawl       ####
# ##############################################
# TODO: Version Verify
# TODO: Patch Notes
# TODO: Code beautify

from  colorama import Fore
import os
import json
import requests

def downloadAssets(lang):
    import json

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
        file.close()

def langSet(lang):
    from colorama import Fore

    if lang == 1: #english
        print(Fore.RED + '[!] ' + Fore.RESET + 'Downloading English language quizz')
        downloadAssets(str('en'))
    if lang == 2: #spanish
        print(Fore.RED + '[!] ' + Fore.RESET + 'Downloading Spanish language quizz')
        downloadAssets(str('es'))
    if lang == 3: #french
        print(Fore.RED + '[!] ' + Fore.RESET + 'Downloading French language quizz')
        downloadAssets(str('fr'))
    if lang == 4: #germany
        print(Fore.RED + '[!] ' + Fore.RESET + 'Downloading Germany language quizz')
        downloadAssets(str('de'))
    if lang == 5: #italy
        print(Fore.RED + '[!] ' + Fore.RESET + 'Downloading Italy language quizz')
        downloadAssets(str('it')) 
    if lang == 6: #polish
        print(Fore.RED + '[!] ' + Fore.RESET + 'Downloading Polish language quizz')
        downloadAssets(str('pl')) 
    if lang == 7: #portugal
        print(Fore.RED + '[!] ' + Fore.RESET + 'Downloading Portugal language quizz')
        downloadAssets(str('pt'))
    if lang == 8: #turkey
        print(Fore.RED + '[!] ' + Fore.RESET + 'Downloading Turkey language quizz')
        downloadAssets(str('tr'))
    if lang == 9: #russian
        print(Fore.RED + '[!] ' + Fore.RESET + 'Downloading Russian language quizz')
        downloadAssets(str('ru'))
    if lang == 10: #japanesee
        print(Fore.RED + '[!] ' + Fore.RESET + 'Downloading Japanesee language quizz')
        downloadAssets(str('jp'))
    if lang == 11: #???
        print(Fore.RED + '[!] ' + Fore.RESET + 'Downloading Chinesee language quizz')
        downloadAssets(str('zh-sc'))
    if lang == 12: #???
        print(Fore.RED + '[!] ' + Fore.RESET + 'Downloading Chinesee language quizz')
        downloadAssets(str('zh-tc'))
    if lang == 13: #korean
        print(Fore.RED + '[!] ' + Fore.RESET + 'Downloading Korean language quizz')
        downloadAssets(str('kr'))

def main():
    import json

    if os.path.exists('webCache') ==  False:
        os.system('md webCache')
    
    with open('config.json', 'r+', encoding="utf8") as configData:
        fData = json.load(configData)
        configData.close()
        appVersion = fData['version']

    print(
        '-----------------------------\n'
        '|     SELECT A LANGUAGE     |\n'
        '-----------------------------\n'
        '| INDEX |     LANGUAGE      |\n'
        '-----------------------------\n'
        '|   1   | English           |\n'
        '|   2   | Español           |\n'
        '|   3   | Français          |\n'
        '|   4   | Deutsch           |\n'
        '|   5   | Italiano          |\n'
        '|   6   | Polski            |\n'
        '|   7   | Português         |\n'
        '|   8   | Türkçe            |\n'
        '|   9   | Pусский           |\n'
        '|   10  | 日本語            |\n'
        '|   11  | 简体中文          |\n'
        '|   12  | 繁體中文          |\n'
        '|   13  | 한국어            |\n'
        '-----------------------------\n'
        f'Tool Version: {appVersion}'
    )
    langPick = int(input('QUIZZ Language: '))

    langSet(langPick)

    os.system('cls')

    jsonTexts = open('webCache\\texts.json')
    quizzDB = json.load(jsonTexts)
    jsonTexts.close()
    os.system('rmdir /s /q webCache')

    questionNum = 1

    while questionNum >=1 and questionNum <= 9:
        questionNumSTR = str(questionNum)
        try:
            qTitle = quizzDB['q000'+questionNumSTR+'_title']
            qAnswer1 = quizzDB['q000'+questionNumSTR+'_answer_1']
            qAnswer2 = quizzDB['q000'+questionNumSTR+'_answer_2']
            qAnswer3 = quizzDB['q000'+questionNumSTR+'_answer_3']
            qAnswer4 = quizzDB['q000'+questionNumSTR+'_answer_4']
        except KeyError:
            pass
        try:
            print(
                Fore.GREEN+questionNumSTR+'. '+qTitle+'\n'+Fore.RESET,
                Fore.CYAN+'    A. '+qAnswer1+'\n'+Fore.RESET,
                Fore.CYAN+'    B. '+qAnswer2+'\n'+Fore.RESET,
                Fore.CYAN+'    C. '+qAnswer3+'\n'+Fore.RESET,
                Fore.CYAN+'    D. '+qAnswer4+Fore.RESET+'\n'
            )
        except NameError:
            pass
        try:
            del qTitle
            del qAnswer1
            del qAnswer2
            del qAnswer3
            del qAnswer4
        except NameError:
            pass
        questionNum = questionNum+1

    while questionNum >=10 and questionNum <=99:
        questionNumSTR = str(questionNum)
        try:
            qTitle = quizzDB['q00'+questionNumSTR+'_title']
            qAnswer1 = quizzDB['q00'+questionNumSTR+'_answer_1']
            qAnswer2 = quizzDB['q00'+questionNumSTR+'_answer_2']
            qAnswer3 = quizzDB['q00'+questionNumSTR+'_answer_3']
            qAnswer4 = quizzDB['q00'+questionNumSTR+'_answer_4']
        except KeyError:
            pass
        try:
            print(
                Fore.GREEN+questionNumSTR+'. '+qTitle+'\n'+Fore.RESET,
                Fore.CYAN+'    A. '+qAnswer1+'\n'+Fore.RESET,
                Fore.CYAN+'    B. '+qAnswer2+'\n'+Fore.RESET,
                Fore.CYAN+'    C. '+qAnswer3+'\n'+Fore.RESET,
                Fore.CYAN+'    D. '+qAnswer4+Fore.RESET+'\n'
            )
        except NameError:
            pass
        try:
            del qTitle
            del qAnswer1
            del qAnswer2
            del qAnswer3
            del qAnswer4
        except NameError:
            pass
        questionNum = questionNum+1

    while questionNum >=100 and questionNum <=999:
        questionNumSTR = str(questionNum)
        try:
            qTitle = quizzDB['q0'+questionNumSTR+'_title']
            qAnswer1 = quizzDB['q0'+questionNumSTR+'_answer_1']
            qAnswer2 = quizzDB['q0'+questionNumSTR+'_answer_2']
            qAnswer3 = quizzDB['q0'+questionNumSTR+'_answer_3']
            qAnswer4 = quizzDB['q0'+questionNumSTR+'_answer_4']
        except KeyError:
            pass
        try:
            print(
                Fore.GREEN+questionNumSTR+'. '+qTitle+'\n'+Fore.RESET,
                Fore.CYAN+'    A. '+qAnswer1+'\n'+Fore.RESET,
                Fore.CYAN+'    B. '+qAnswer2+'\n'+Fore.RESET,
                Fore.CYAN+'    C. '+qAnswer3+'\n'+Fore.RESET,
                Fore.CYAN+'    D. '+qAnswer4+Fore.RESET+'\n'
            )
        except NameError:
            pass
        try:
            del qTitle
            del qAnswer1
            del qAnswer2
            del qAnswer3
            del qAnswer4
        except NameError:
            pass
        questionNum = questionNum+1

    while questionNum >=1000 and questionNum <=9999:
        questionNumSTR = str(questionNum)
        try:
            qTitle = quizzDB['q'+questionNumSTR+'_title']
            qAnswer1 = quizzDB['q'+questionNumSTR+'_answer_1']
            qAnswer2 = quizzDB['q'+questionNumSTR+'_answer_2']
            qAnswer3 = quizzDB['q'+questionNumSTR+'_answer_3']
            qAnswer4 = quizzDB['q'+questionNumSTR+'_answer_4']
        except KeyError:
            pass
        try:
            print(
                Fore.GREEN+questionNumSTR+'. '+qTitle+'\n'+Fore.RESET,
                Fore.CYAN+'    A. '+qAnswer1+'\n'+Fore.RESET,
                Fore.CYAN+'    B. '+qAnswer2+'\n'+Fore.RESET,
                Fore.CYAN+'    C. '+qAnswer3+'\n'+Fore.RESET,
                Fore.CYAN+'    D. '+qAnswer4+Fore.RESET+'\n'
            )
        except NameError:
            pass
        try:
            del qTitle
            del qAnswer1
            del qAnswer2
            del qAnswer3
            del qAnswer4
        except NameError:
            pass
        questionNum = questionNum+1

main()