import os
from time import sleep
import winsound
import subprocess
import sys
import time

version = "1.0"
file = "Sound/bip.wav"

def typewriter(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

os.system('cls')
typewriter("Instalation cela peut prendre plus ou moin de temps ..........", delay=0.05)
os.system("pip install -r requirements.txt")
os.system('cls')

# Utilisation
winsound.PlaySound(file, winsound.SND_FILENAME)
typewriter("SalmonPY - Chargement en cours......", delay=0.05)
winsound.PlaySound(file, winsound.SND_FILENAME)
typewriter(version, delay=0.3)
sleep(1)

def menuprincipal():
    os.system('cls')
    typewriter("BIENVENUE DANS LE MENU PRINCIPAL", delay=0.05)
    typewriter("Voici les option", delay=0.05)
    typewriter("1:Compilation phyton", delay=0.05)
    option = input("Veuiller selectioner une option : ")

    if option == "1":
        os.system("py2exe-gui")
        sleep(1)
        os.system('cls')

    else:
        print ("Option invalide")
        sleep(1)
        menuprincipal()

menuprincipal()