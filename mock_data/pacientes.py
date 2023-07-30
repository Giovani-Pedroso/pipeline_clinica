# from random import randrange
from numpy import random
import time
from datetime import timedelta, datetime
import os
from dotenv import load_dotenv 
from random import choice, randint
import pandas as pd
load_dotenv()

PLANINHA_CLIENTES = os.getenv('PLANINHA_CLIENTES')
DATA_INICIAL = datetime.today().strftime('%d/%m/%Y') 
DATA_ATUAL= "30/7/2023" 

#Creates a mockdata for testing the program
#the original has sensible information, so it was 
#decided to use fake data only to test
def create_mock(number_of_entries):
    #the entries are in protuguese 
    #First name, surname, age, state or province, phone, number of *****,
    #first *****, last *****, date of birth, origin(how the patient found the clinics
    # Social midias, plataform, website, indication),
    #job, civil state***, gender


    # df = pd.DataFrame(columns=columns)    
    # print(df)
    
    patients = []

    for _ in range(number_of_entries):
        patients.append(create_fake_patient())

    df = pd.DataFrame.from_dict(patients)
    df.to_excel(PLANINHA_CLIENTES)
    print(df)

#Create a patient with random information
def create_fake_patient():
    global primeiro_nome  

    #So mock infromation to create 
    #a fake patient
    #Male names
    primeiro_nomes_h = ['João', 'Pedro', 'Lucas',
                        'Carlos', 'Fabio', 'Mario',
                        'Manuel', 'Thiago', 'Jean']

    #Female names
    primeiro_nomes_m = ['Fabia', 'Ana', 'Carol',
                        'Maria', 'Katia','Eliza',
                        'Leticia','Beatriz', 'Simone']
    #M - mulher(woman in portuguese)
    #H - homem(man in portuguese)
    genero = choice(['M', 'H'])
    if genero == "M":
        primeiro_nome = choice(primeiro_nomes_m)
    else:
        primeiro_nome = choice(primeiro_nomes_h)


    sobrenome = choice(['Silva', 'Oliveira', 'Santos',
                   'Cardoso', 'Souza','Rodrigues',
                   'Pereira', 'Lima', 'Gomes'])

    origem = choice(['Plataforma', 'Indicação', 'Midias Sociais', 'Site'])
    proficao = choice(['Medico', 'Policial', 'Advogado', 'Jornalista'])
    estado_civil= choice(['solteiro', 'casado','viuvo','divorciado', 'uniao'])
    estado = choice(['SP','RJ', "CE", "GO", 'EX', 'AM'])
    idade = randint(18, 60)
    n_consultas = randint(1, 48)

    
    primeira_consulta= random_date(DATA_INICIAL, DATA_ATUAL, random.random())    
    ultima_consulta = random_date('6/1/2023', DATA_ATUAL, random.random())
    data_nascimento= random_date('1/1/1970', '31/12/2002', random.random())

    return {'primeiro nome':primeiro_nome, 
            'sobrenome': sobrenome,
            'idade':idade,
            'estado de residencia':estado,
            'tel':"99 99999-9999",
            'numero de consultas':n_consultas,
            'primeira consulta':primeira_consulta,
            'ultima consulta':ultima_consulta,
            'data de nascimento':data_nascimento,
            'origem':origem,
            'profição':proficao,
            'estado civil':estado_civil,
            'genero':genero
            }

def str_time_prop(start, end, time_format, prop):
    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))
    ptime = stime + prop * (etime - stime)
    return time.strftime(time_format, time.localtime(ptime))
 
 
def random_date(start, end, prop):
    return str_time_prop(start, end, '%d/%m/%Y', prop)

create_mock(140)
