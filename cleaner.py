#Importar Bibilhotecas
import json
import os
import requests

#Define o arquivo de configuração
configfile = 'cfg'
configpath = os.path.join(os.getcwd(), f'{configfile}.ini')
logpath = os.path.join(os.getcwd(), f'log.txt')

try:
    ckey = requests.get('https://raw.githubusercontent.com/LuGB18/AutoCleanerPy/main/clperm.key')
    ckey.raise_for_status()
    ckey = json.load(ckey.content())
except requests.exceptions.RequestException:
    with open(logpath, 'w') as log:
                log.write(f'''
                                An unexpected error has occured.
                                Please ensure you have a conection with the internet.                
                                ''')
                exit()


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
                            Please contact the Repo Owner to advise of the error.
                            Error:{e}                   
                            ''')
                exit()
        
else:
    with open(configpath, 'w') as cfg:
        cfg.write(json.dumps([{'key': ''}], indent=4))
        
if not config['key'] == ckey['key']:
     with open(logpath, 'w') as log:
                log.write(f'''
                            An unexpected error has occured.
                            Please ensure you key is valid.
                            Error:{e}                   
                            ''')
                exit()
