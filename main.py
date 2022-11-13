from lib import fileMenager
import os

if os.path.exists('webCache') ==  False:
    os.system('md webCache')

print(
    '-----------------------------\n'
    '|     SELECT A LANGUAGE     |\n'
    '-----------------------------\n'
    '| INDEX |     LANGUAGE      |\n'
    '-----------------------------\n'
    '|   1   | English           |'+'-works\n'
    '|   2   | Español           |'+'-error\n'
    '|   3   | Français          |'+'-error\n'
    '|   4   | Deutsch           |'+'-works\n'
    '|   5   | Italiano          |'+'-error\n'
    '|   6   | Polski            |'+'-works\n'
    '|   7   | Português         |'+'-error\n'
    '|   8   | Türkçe            |'+'-error\n'
    '|   9   | Pусский           |'+'-error\n'
    '|   10  | 日本語            |'+'-error\n'
    '|   11  | 简体中文          |'+'-error\n'
    '|   12  | 繁體中文          |'+'-error\n'
    '|   13  | 한국어            |'+'-error\n'
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

fileMenager.download(str(lang))
