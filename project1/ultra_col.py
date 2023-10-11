#!/usr/bin/env python3

import argparse
from time import time, ctime
import datetime
import random
import string
from nltk.corpus import words
from collections import namedtuple
from pprint import pprint
from readchar import readkey
import readchar
from datetime import datetime
from colorama import Fore, Back, Style
#nltk.download('words')

from nltk.corpus import words

# Define o namedtuple Input

Input = namedtuple('Input', ['requested', 'received', 'duration'])

def obtain_input_answer(x,random_word, bem_sucedido,input_records):

    start_time = time()

    if x == 1:
    
        keys = []

        keys = ""
        tti = time()
        
        print(f"Digite: {random_word} : ",end = "",flush=True) 


        while len(keys) < len(random_word):

            key = readchar.readchar()
            if ord(key) == 32:
                break
        
            keys += key

            print(key, end = "",flush=True)   
            
        print() 
         

        if keys == random_word:
            print(Fore.GREEN+ f"Correto! " + Style.RESET_ALL + "Voce inseriu " + Fore.GREEN + f"{keys}" + Style.RESET_ALL)
            bem_sucedido += 1
        elif ord(key) == 32:
            print(Fore.YELLOW + f"Teste cancelado" + Style.RESET_ALL)

           
        else:
            print(Fore.RED + f"Incorreto! "+ Style.RESET_ALL + "Voce inseriu " + Fore.RED + f"{keys}" + Style.RESET_ALL)

        ttf = time()
        tempo_tentativa = round(ttf-tti,2)   

        input_record = Input(requested=random_word, received=keys, duration=tempo_tentativa)
        input_records.append(input_record)  # Adicione o registro à lista        
        
        
  

    else:

        tti = time()

        print(f"Digite: {random_word} ")

        key = readkey()

        if key == random_word:
            print(Fore.GREEN + f"Correto! " + Style.RESET_ALL + "Voce inseriu " + Fore.GREEN + f"{key}" + Style.RESET_ALL)
            bem_sucedido += 1

        elif ord(key) == 32:
            print(Fore.YELLOW + f"Teste cancelado" + Style.RESET_ALL)
           
        else:
            print(Fore.RED + f"Incorreto! " + Style.RESET_ALL + "Voce inseriu " +Fore.RED + "{key}" + Style.RESET_ALL)

        ttf = time()
        tempo_tentativa = round(ttf-tti,2)     
  
        input_record = Input(requested=random_word, received=key, duration=tempo_tentativa)
        input_records.append(input_record)  # Adicione o registro à lista

    return bem_sucedido, key, input_records      

def temp_mx( bem_sucedido, tempo_decorrido): 

    args = arg_init()
    input_records = []
    x=0 
    number_of_types=0
    bem_sucedido=0
    start_time= time()
    while True:

        tempo_inicio=time()
        
        if args.use_words:
            x=1
            random_word = generate_random_word()
        else:
            random_word = random.choice(string.ascii_lowercase)
        
        bem_sucedido, key, input_records = obtain_input_answer(x,random_word, bem_sucedido,input_records)
        input_ascii = ord(key)

        tempo_fim=time()
        tempo_tentativa=  round(tempo_fim- tempo_inicio ,2)

        if input_ascii == 32:
            break

        number_of_types +=1
 
        
        end_time=time()
        tempo_decorrido= round(end_time - start_time, 2)

        if tempo_decorrido >= args.max_value:
            break    
        

    print(f"De {number_of_types} tentativas voce acertou  " + Fore.GREEN + f"{bem_sucedido}" +Style.RESET_ALL+ f"em {tempo_decorrido} segundos.")   
    return number_of_types, bem_sucedido, tempo_decorrido, input_records  


def input_mx( bem_sucedido, tempo_decorrido): 

    args = arg_init()
    input_records = []
    x=0 # oque faz??
    number_of_types=0
    bem_sucedido=0 
    start_time=time()

    while True:
        tempo_inicio=time()
        if args.use_words:
            x=1
            random_word = generate_random_word()
        else:
            random_word = random.choice(string.ascii_lowercase)
        
        bem_sucedido, key, input_records = obtain_input_answer(x,random_word, bem_sucedido,input_records)

        input_ascii = ord(key)

        tempo_fim=time()
        tempo_decorrido=  round(tempo_fim- tempo_inicio ,2)

        if input_ascii == 32:

            break

        number_of_types +=1


        if number_of_types >= args.max_value:
            break    

    end_time=time()
    tempo_decorrido= round(end_time - start_time, 2)   
   

    print(f"De {number_of_types} tentativas voce acertou " + Fore.GREEN + f"{bem_sucedido}" + Style.RESET_ALL + f" em {tempo_decorrido} segundos.")   
    return number_of_types, bem_sucedido, tempo_decorrido, input_records   


def generate_random_word():
    

     word_list = words.words()
     random_word= random.choice(word_list)
     return random_word.lower()

def arg_init():

    # Configurar o parser de argumentos de entrada

    parser = argparse.ArgumentParser(description="Definição do modo de teste")

    parser.add_argument("-utm", "--use_time_mode", action="store_true",
                        help="Tempo máximo em segundos para o modo de tempo ou número máximo de entradas para o modo de número de entradas.")
    parser.add_argument("-mv", "--max_value", type=int,
                        help="Tempo máximo em segundos para o modo de tempo ou número máximo de entradas para o modo de número de entradas.")
    parser.add_argument("-uw", "--use_words", action="store_true",
                        help="Usar o modo de digitação de palavras em vez de digitação de caracteres individuais.")
    
    return parser.parse_args()     

def aguardar_tecla():

    print("Pressione uma tecla para começar o desafio...")

    digitado = readkey()
#############################    MAIN    #######################

def main():

    # Variaveis

    test_start = ctime()
    tentativa = 0
    bem_sucedido = 0
    tempo_decorrido =0
    
    #Chamada da função arg_init()
       
    args = arg_init()

    print("Tempo Máximo:", args.max_value)
    print("time mode:", args.use_time_mode)
    print("use words:", args.use_words)

    aguardar_tecla()

    # Atribuir o length
   

    if args.use_time_mode:

        number_of_types, bem_sucedido, tempo_decorrido, input_records = temp_mx( bem_sucedido, tempo_decorrido)

    else:

        number_of_types, bem_sucedido, tempo_decorrido, input_records = input_mx(bem_sucedido,tempo_decorrido) 



    # Statistic

    accuracy = str(round((bem_sucedido / number_of_types)* 100)) + '%' if number_of_types > 0 else str(0) + '%'
    type_average_duration = round(sum(input_record.duration for input_record in input_records) / number_of_types, 2) if number_of_types > 0 else 0

    type_hit_average_duration = round(sum(input_record.duration for input_record in input_records if input_record.requested == input_record.received and bem_sucedido > 0) / bem_sucedido , 2) if bem_sucedido > 0 else 0

    type_miss_average_duration = round(sum(input_record.duration for input_record in input_records if input_record.requested != input_record.received and number_of_types - bem_sucedido > 0) / (number_of_types - bem_sucedido), 2) if number_of_types - bem_sucedido > 0 else 0


    test_end = ctime()

    result_dict = {
        'accuracy': accuracy,
        'inputs': input_records,
        'number_of_hits': bem_sucedido,
        'test_duration': tempo_decorrido,
        'test_start': test_start,
        'test_end': test_end,
        'number_of_types': number_of_types,
        'type_average_duration': type_average_duration,
        'type_hit_average_duration': type_hit_average_duration,
        'type_miss_average_duration': type_miss_average_duration
        }      
    pprint(result_dict)

    
if __name__ == "__main__":
    main() 
