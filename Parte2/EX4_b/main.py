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

def ReadCharsUpTo(Stop_char):
    chars = []
    while True:
        chars.append(readchar.readchar())
        print(chars[-1])
        if chars[-1] == Stop_char:
                 break

def main():

  ReadCharsUpTo('x')


if __name__ == "__main__":
    main()