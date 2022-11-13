from lib import fileMenager
import os

if os.path.exists('webCache') ==  False:
    os.system('md webCache')

fileMenager.download()
