from  colorama import Fore
import os
import json
import requests

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
        file.close()

def main():
    if os.path.exists('webCache') ==  False:
        os.system('md webCache')

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
        '-----------------------------'
    )
    langPick = int(input('QUIZZ Language: '))

    if langPick == 1: #english
        lang = str('en')
    if langPick == 2: #spanish
        lang = str('es')
    if langPick == 3: #french
        lang = str('fr')
    if langPick == 4: #germany
        lang = str('de') 
    if langPick == 5: #italy
        lang = str('it') 
    if langPick == 6: #polish
        lang = str('pl') 
    if langPick == 7: #portugal
        lang = str('pt')
    if langPick == 8: #turkey
        lang = str('tr')
    if langPick == 9: #russian
        lang = str('ru')
    if langPick == 10: #japanesee
        lang = str('jp')
    if langPick == 11: #???
        lang = str('zh-sc')
    if langPick == 12: #???
        lang = str('zh-tc')
    if langPick == 13: #korean
        lang = str('kr')

    os.system('cls')
    downloadTexts(str(lang))

    jsonTexts = open('webCache\\texts.json')
    quizzDB = json.load(jsonTexts)

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