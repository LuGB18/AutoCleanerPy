#Importar Bibilhotecas
import json
import os
import requests
from glob import glob

#Define o arquivo de configuração
configfile = 'cfg'
ckey = requests.get('')

if os.path.exists(os.path.join(os.getcwd(), f'{configfile}.ini')):
    with open(os.path.join(os.getcwd(), f'{configfile}.ini'), 'r') as cfg:
        try:
            config = json.loads(cfg.read())
        except json.decoder.JSONDecodeError:
            with open(os.path.join(os.getcwd(), f'log.txt'), 'w') as log:
                log.write(f'''
                                An unexpected error has occured.
                                Please re-enter your key on the "{configfile}.ini" file and re-open the program.                
                                ''')
                log.close()
                exit()
        except Exception as e:
            with open(os.path.join(os.getcwd(), f'log.txt'), 'w') as log:
                log.write(f'''
                            An unexpected error has occured.
                            Please contact the Repo Owner to advise of the error.
                            Error:{e}                   
                            ''')
                log.close()
                exit()
        cfg.close()
else:
    with open(os.path.join(os.getcwd(), f'{configfile}.ini'), 'w') as cfg:
        cfg.write(json.dumps([{'key': ''}], indent=4))
        cfg.close()
