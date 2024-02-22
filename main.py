import webbrowser
import os
webbrowser.open("https://discord.gg/murphys")
try:
    import pystyle
except ImportError:
    print("Le module pystyle n'est pas installé. Installation en cours...")
    os.system('pip install pystyle')
    import pystyle
try:
    import requests
except ImportError:
    print("Le module requests n'est pas installé. Installation en cours...")
    os.system('pip install requests')
    import requests

import pystyle
import requests
import json
import time
from pystyle import *

def clear():
    os.system('cls')

def main():
    while True:
        with open('config.json') as config_file:
            config = json.load(config_file)
            webhook = config['webhook']
            name = config['name']
            pp = config['pp']
            
            if pp == "":
                pp = None
            if name == "":
                name = None
            if webhook == "":
                webhook = input('Veuillez entrer un webhook >>')
                
                config['webhook'] = webhook
                json.dump(config, open('config.json', 'w'), indent=1)
        clear()
        banner = int(input(Colorate.Horizontal(Colors.rainbow, """
███╗   ███╗██╗   ██╗██████╗ ██████╗ ██╗  ██╗██╗   ██╗███████╗    ███████╗██████╗  █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗ 
████╗ ████║██║   ██║██╔══██╗██╔══██╗██║  ██║╚██╗ ██╔╝██╔════╝    ██╔════╝██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗
██╔████╔██║██║   ██║██████╔╝██████╔╝███████║ ╚████╔╝ ███████╗    ███████╗██████╔╝███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝
██║╚██╔╝██║██║   ██║██╔══██╗██╔═══╝ ██╔══██║  ╚██╔╝  ╚════██║    ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗
██║ ╚═╝ ██║╚██████╔╝██║  ██║██║     ██║  ██║   ██║   ███████║    ███████║██║     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║
╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝   ╚═╝   ╚══════╝    ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝
                                                        discord.gg/murphys
                                               
                                            [1] Spam webhook
                                            [2] Modifier la config
                                            [3] Quitter le tool

                                               

    >>""")))
        if banner == 1:
            choice = input(Colorate.Horizontal(Colors.rainbow, f"""
Voici votre configuration actuelle :
    Webhook: {webhook}
    Nom: {name}
    Photo de profil: {pp}
Êtes-vous sur de vouloir continuer ? (y/n) : """))
            if choice == "y":
                message = input(Colorate.Horizontal(Colors.rainbow, f"Quel message voulez vous envoyer ? :"))
                amount = int(input(Colorate.Horizontal(Colors.rainbow, f"Combien de fois voulez vous envoyer le message (0 pour infini) ? :")))
                clear()
                data = {
                    "content": message,
                    "username": name,
                    "avatar_url": pp
                }
                if amount > 0:
                    x=0
                    for x in range(amount):
                        response = requests.post(webhook, json=data)
                        if response.status_code == 204:
                            x+=1
                            os.system('color a')
                            print(f"{message} envoyé {x} fois.")
                        else:
                            if response.status_code == 429:
                                print("Le tool envoie trop de requêtes.")
                                print(">> 10")
                                time.sleep(1)
                                print(">> 9")
                                time.sleep(1)
                                print(">> 8")
                                time.sleep(1)
                                print(">> 7")
                                time.sleep(1)
                                print(">> 6")
                                time.sleep(1)
                                print(">> 5")
                                time.sleep(1)
                                print(">> 4")
                                time.sleep(1)
                                print(">> 3")
                                time.sleep(1)
                                print(">> 2")
                                time.sleep(1)
                                print(">> 1")
                                time.sleep(1)
                            else:
                                print(f"Échec de l'envoi du message. Code d'erreur : {response.status_code}")
                    os.system('color 7')
                if amount == 0:
                    x=0
                    while True:
                        response = requests.post(webhook, json=data)
                        if response.status_code == 204:
                            x+=1
                            os.system('color a')
                            print(f"{message} envoyé {x} fois.")
                        else:
                            if response.status_code == 429:
                                print("Le tool envoie trop de requêtes.")
                                print(">> 10")
                                time.sleep(1)
                                print(">> 9")
                                time.sleep(1)
                                print(">> 8")
                                time.sleep(1)
                                print(">> 7")
                                time.sleep(1)
                                print(">> 6")
                                time.sleep(1)
                                print(">> 5")
                                time.sleep(1)
                                print(">> 4")
                                time.sleep(1)
                                print(">> 3")
                                time.sleep(1)
                                print(">> 2")
                                time.sleep(1)
                                print(">> 1")
                                time.sleep(1)
                            else:
                                print(f"Échec de l'envoi du message. Code d'erreur : {response.status_code}")
        if banner == 2:
            while True:
                clear()
                banner2 = int(input(Colorate.Horizontal(Colors.rainbow, """
███╗   ███╗██╗   ██╗██████╗ ██████╗ ██╗  ██╗██╗   ██╗███████╗    ███████╗██████╗  █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗ 
████╗ ████║██║   ██║██╔══██╗██╔══██╗██║  ██║╚██╗ ██╔╝██╔════╝    ██╔════╝██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗
██╔████╔██║██║   ██║██████╔╝██████╔╝███████║ ╚████╔╝ ███████╗    ███████╗██████╔╝███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝
██║╚██╔╝██║██║   ██║██╔══██╗██╔═══╝ ██╔══██║  ╚██╔╝  ╚════██║    ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗
██║ ╚═╝ ██║╚██████╔╝██║  ██║██║     ██║  ██║   ██║   ███████║    ███████║██║     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║
╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝   ╚═╝   ╚══════╝    ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝
                                                        discord.gg/murphys

                                            [1] Modifier le webhook
                                            [2] Modifier le nom
                                            [3] Modifier la pp
                                            [4] Tout modifier
                                            [5] Retourner au menu

    >>""")))
                if banner2 == 1:
                    webhook = input(Colorate.Horizontal(Colors.rainbow, "Nouveau webhook : "))
                    config['webhook'] = webhook
                    json.dump(config, open('config.json', 'w'), indent=1)
                if banner2 == 2:
                    name = input(Colorate.Horizontal(Colors.rainbow, "Nouveau nom : "))
                    config['name'] = name
                    json.dump(config, open('config.json', 'w'), indent=2)
                if banner2 == 3:
                    pp = input(Colorate.Horizontal(Colors.rainbow, "Nouvelle pp (lien) : "))
                    config['pp'] = pp
                    json.dump(config, open('config.json', 'w'), indent=3)
                if banner2 == 4:
                    webhook = input(Colorate.Horizontal(Colors.rainbow, "Nouveau webhook : "))
                    config['webhook'] = webhook
                    json.dump(config, open('config.json', 'w'), indent=1)
                    name = input(Colorate.Horizontal(Colors.rainbow, "Nouveau nom : "))
                    config['name'] = name
                    json.dump(config, open('config.json', 'w'), indent=2)
                    pp = input(Colorate.Horizontal(Colors.rainbow, "Nouvelle pp (lien) : "))
                    config['pp'] = pp
                    json.dump(config, open('config.json', 'w'), indent=3)
                if banner2 == 5:
                    main()
        if banner == 3:
            exit()
main()
