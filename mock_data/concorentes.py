# from random import randrange
from numpy import random
from datetime import datetime
import time
from datetime import timedelta, datetime
import os
from dotenv import load_dotenv 
from random import choice
import pandas as pd
load_dotenv()

DB_RANKING= os.getenv('DB_RANKING')
DB_PSICOLOGOS= os.getenv('DB_PSICOLOGOS')

psicologos = ['clinica-ef','maria-gomes','beatriz-rodrigues', 'fabio-silva', 
              'manuel-santos', 'lucas-cardoso', 'lucas-santos',
              'fabia-cardoso', 'fabio-cardoso', 'simone-souza',
              'maria-silva', 'carol-lima', 'fabia-souza',
              'beatriz-souza', 'manuel-lima', 'lucas-pereira',
              'maria-pereira', 'pedro-oliveira', 'keticia-lima',
              'eliza-pereira', 'mario-pereira', 'eliza-lima', 
              'jean-rodrigues', 'thiago-lima', 'joao-lima',
              'simone-silva', 'beatriz-pereira',]

#Create an entry of the table
new_entry = []
date_todayo= datetime

# def mock_entry(): 
for _ in range(20):

    psi = choice(psicologos)
    
    while psi in new_entry:
        psi = choice(psicologos)
    
    new_entry.append(psi)

print(new_entry)

def generate_fake_psi(number):
    primeiro_nomes = ['joao', 'pedro', 'lucas',
                      'farlos', 'fabio', 'mario',
                      'manuel', 'thiago', 'jean',
                      'fabia', 'ana', 'carol',
                      'maria', 'katia','eliza',
                      'keticia','beatriz', 'simone']
    
    sobrenome = ['silva', 'oliveira', 'santos',
                   'cardoso', 'souza','rodrigues',
                   'pereira', 'lima', 'gomes']
    print('psicologos = [')
    for _ in range(number):
        print(f" '{choice(primeiro_nomes)}-{choice(sobrenome)}',")
    print(']')

#Uncoment this line to generate fake doctors
# generate_fake_psi(26)

#primary ke- tempo salvo em intervalos de 30min, 1 place, 2 second place, 3 place 
