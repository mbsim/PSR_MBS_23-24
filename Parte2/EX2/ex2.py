#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python

#use imports here
from colorama import Fore, Back, Style

from my_functions import isPerfect
from my_functions import isPrime

# define functions here ...

maximum_number = 10



def main():
    print("Starting to compute perfect numbers up to " + str(maximum_number))

    for i in range(1, maximum_number):
        if isPerfect(i):
            print('Number ' + str(i) + ' is perfect.')

    for i in range(1, maximum_number):
        if isPrime(i):
            print('Number ' + str(i) + ' is Prime.')        


if __name__ == "__main__":
    main()