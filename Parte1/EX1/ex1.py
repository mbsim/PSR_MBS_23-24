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

def main(x,random_word):

    if x == 1:
    
        keys = []

        keys = ""
        
        ti = time()
        print(f"Digite: {random_word} : ",end = "",flush=True) 


        while len(keys) < len(random_word):

            key = readchar.readchar()
        
            keys += key

            print(key, end = "",flush=True)   
            
        print()          

        if keys == random_word:
            print(f"Correto, voce inseriu! {keys}")
            bem_sucedido += 1
           
        else:
            print("Incorreto. Tente novamente.") 

        tf = time()      

    else:

        print(f"Digite: {random_word} ")

        ti = time()

        key = readkey()

        if key == random_word:
            print(f"Correto, voce inseriu! {key}")
            bem_sucedido += 1
        else:
            print("Incorreto. Tente novamente.")

        tf = time()    



if __name__ == "__main__":
    main()