#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python

# --------------------------------------------------
# A simple python script to print hello world!
# Miguel Riem Oliveira.
# PSR, September 2023.
# --------------------------------------------------

import argparse

import readchar

# Passo 1: ler um carater do terminal -> readchar 

def printAllCharsUpTo():

    print("Digita um numero: ")
    key = readchar.readkey()

    print(f"O utilizador pressionou: {key}") # Digitar o carater no terminal 

# Passo 2: lido -> char? calcular o número correspondente ao lido  chr ou ord    

    number = ord(key)           #A função ‘ord’ em Python é utilizada para obter o valor numérico  
                                #de um caractere. Isso pode ser útil em várias situações, como quando se 
                                # precisa comparar caracteres ou realizar operações específicas que envolvam valores ASCII.  
    
    print(f"Corresponding Number is: {number}") # Digitar o correspondete do numero no terminal 

# passo 3: percorrer todos os numeros deste o espaço (32) até ao nmero lido, e para cada iteração imprimir o carater correspondente    

    for i in range(32,number):
        print(chr(i))

def main():

    printAllCharsUpTo()


if __name__ == "__main__":
    main()