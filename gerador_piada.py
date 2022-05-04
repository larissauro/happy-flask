
from unidecode import unidecode #leitura de acentos e caracteres especiais
from time import sleep
from os import listdir
import random
from random import shuffle

def generate_piada():
    banco = open ("Piadas.txt" , "r", encoding="UTF-8" )
    numero = int(banco.readline())
    lista = banco.read().split('\n')


    piada = lista[numero]

    numero = numero + 1

    if numero == len(lista):
        shuffle(lista)
        numero = 0

    with open("Piadas.txt", 'w', encoding="UTF-8") as file:
        file.writelines(str(numero) + '\n')
        
        file.write('\n'.join(lista))
    return piada