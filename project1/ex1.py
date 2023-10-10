import argparse
from time import time
import datetime
from readchar import readkey
import random
import string
from nltk.corpus import words
from collections import namedtuple
from pprint import pprint
import sys

def le_palavra_ate_bola():
    palavra = ""
    while palavra != "bola":
        try:
            palavra = sys.argv[1]
        except IndexError:
            print("Digite uma palavra:")
            palavra = input()
    print(palavra)        
    print("correto'!")

def main():


    le_palavra_ate_bola()


if __name__ == "__main__":
    main()

