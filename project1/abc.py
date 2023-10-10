import argparse
from time import time
import datetime
import readchar
import random
import string
from nltk.corpus import words
from collections import namedtuple
from pprint import pprint
import sys
from readchar import readkey



def main():
    keys = []

    

    random_caracter = "bola"
    resultado = ""
    keys = ""
        

    print(f"Digite: {random_caracter} : ",end = "",flush=True) 


    while len(keys) < len(random_caracter):

        key = readchar.readchar()
        #abc = readkey()
        
        keys += key
        print(key, end = "",flush=True)
        #print()
            
    print()    
             
            
        #key_string = ', '.join(keys)   
            #resultado = "".join(keys)
            #print(resultado, end ="",flush=True)        

    if keys == random_caracter:
        print(f"Correto, voce inseriu! {keys}")
           
    else:
        print("Incorreto. Tente novamente.")

if __name__ == "__main__":
    main()