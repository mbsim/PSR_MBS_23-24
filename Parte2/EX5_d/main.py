#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python

# --------------------------------------------------
# A simple python script to print hello world!
# Miguel Riem Oliveira.
# PSR, September 2023.
# --------------------------------------------------

import argparse

import readchar

# Use imports here
from colorama import Fore, Back, Style

# Define functions here ...

# maximum_number = 30

def  countNumbersUpto(stop_char):

    print('Start typing')

    keys =[]   
    numerico = []  
                                 #criar um lista chamada keys
    while True:                               #Enquanto nao for digitao o stop_char manter dentro do while true infinitivamente   
        key = readchar.readkey()              #Ler e guaradr o que o utizador colocou no terminal e guardar na variavel key
        keys.append(key)                      #adicionar a key introduzida na lista keys                      
        print('You typed ' + key)             #printar o que foi introduzido

        if key == stop_char:
            break

    print(keys)                               #Printar a Lista

    total_numbers = 0
    total_others = 0

    for key in keys:                          #Criar ciclo for para encontrar numeros na lista e somala numa variavel n_numeric
        if key.isnumeric():
            total_numbers +=1
            numerico.append(key)
        else:
            total_others +=1
    
        

    print('You entered ' + str(total_numbers) + ' numbers.')
    print('You entered ' + str(total_others) + ' others.')
    numerico.sort() #Funcao que permite ordenar por ordem crecente a lista
    print(numerico)
    numericalkeys2 = [x for x in key if x.isnumeric()]  #alinea e listcomprehension
    print("numericalkeys2 = ", +str(numericalkeys2))
    print(numericalkeys2)
        
    #print('You pressed on ' + str(n_numeric) + ' numeric keys')

def main():
    countNumbersUpto('x')


if __name__ == "__main__":
    main()