#!/usr/bin/env python3

from colorama import Fore, Back, Style

maximum_number = 100

def isPerfect(value):
    
    # Percorrer todos os numeros até ao número em análise
    # para cada umero, ver se é um divisor inteiro
    # Se for, somar num acumvalue%i == 0:ulador

    accumulator = 0
    for i in range(1, value):
        if value%i == 0: # its an integer divider
            accumulator = accumulator + i

    # Ver se a soma dos dividores inteiros é igual ao próprio número
    return accumulator == value


    return False

def main():
    print("Starting to compute perfect numbers up to " + str(maximum_number))

    for i in range(0, maximum_number):
        if isPerfect(i):
            print('Number ' + str(i) + ' is perfect.')


if __name__ == "__main__":
    main()