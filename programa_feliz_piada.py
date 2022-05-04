
from unidecode import unidecode #leitura de acentos e caracteres especiais
from time import sleep
from os import listdir
import random
from random import shuffle





def get_piada():
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

def main():
    print("************************************")
    print("Olá, se sentindo triste hoje?")
    print("************************************")


    resposta = unidecode(input("  ")).lower()
    if resposta == "nao" or resposta == "n" :
        print ("Que bom! Continue assim <3")


    elif resposta == "sim" or resposta == "s":

        print("Que pena...:(")
        sleep(2)
        print("Então vou te contar uma coisa engraçada", end='', flush=True)
        sleep(1)
        print(".", end='', flush=True)
        sleep(1)
        print(".", end='', flush=True)
        sleep(1)
        print(".")
        sleep(1)
        printpiada()

if __name__ == "__main__":
	main()
