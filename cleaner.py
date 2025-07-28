#Importar Bibilhotecas
import json
import os
import requests

#Define o arquivo de configuração
configfile = 'cfg'
configpath = os.path.join(os.getcwd(), f'{configfile}.ini')
logpath = os.path.join(os.getcwd(), f'log.txt')

#Baixa a key atual do repositorio e se o server responder qual quer coisa alem de 200 quita.
try:
    ckey = requests.get('https://raw.githubusercontent.com/LuGB18/AutoCleanerPy/main/etc/clperm.key')
    ckey.raise_for_status()
    ckey = json.loads(ckey.content.decode())
except requests.exceptions.RequestException:
    with open(logpath, 'w') as log:
                log.write('''
An unexpected error has occured.
Please ensure you have a conection with the internet.                
''')
                exit()

#Verifica se existe o arquivo Config, se não, cria ele.
if os.path.exists(configpath):
    with open(configpath, 'r') as cfg:
        try:
            config = json.loads(cfg.read())
        except json.decoder.JSONDecodeError:
            with open(logpath, 'w') as log:
                log.write(f'''
An unexpected error has occured.
Please re-enter your key on the "{configfile}.ini" file and re-open the program.                
''')
                exit()
        except Exception as e:
            with open(logpath, 'w') as log:
                log.write(f'''
An unexpected error has occured.
Please contact the Repo Owner to advise of the error
Error:{e}                   
''')
                exit()
        
else:
    with open(configpath, 'w') as cfg:
        cfg.write(json.dumps([{'key': ''}], indent=4))
        exit()

#Verifica se a KEY bate com a do Config.
if not config[0]['key'] == ckey[0]['key']:
     with open(logpath, 'w') as log:
                log.write(f'''
An unexpected error has occured.
Please ensure you key is valid.                   
''')
                exit()