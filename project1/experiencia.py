import argparse
from time import time
import datetime
from readchar import readkey
import random
import string
from nltk.corpus import words
from collections import namedtuple
from pprint import pprint
from readchar import readkey
import readchar
from datetime import datetime
#nltk.download('words')

from nltk.corpus import words

# Define o namedtuple Input

Input = namedtuple('Input', ['requested', 'received', 'duration'])

def obtain_input_answer(x,random_word, bem_sucedido):

    start_time = time()

    if x == 1:
    
        keys = []

        keys = ""
        
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

    else:

        print(f"Digite: {random_word} ")

        key = readkey()

        if key == random_word:
            print(f"Correto, voce inseriu! {key}")
            bem_sucedido += 1
        else:
            print("Incorreto. Tente novamente.")
  
    return bem_sucedido, key      

def temp_mx( bem_sucedido, tempo_decorrido,word_length): 

    args = arg_init()
    input_records = []
    x=0
    number_of_types=0
    bem_sucedido=0
    temponaotenho=1

    while True:

        if args.use_words:
            x=1
            random_word = generate_random_word(word_length)
        else:
            random_word = random.choice(string.ascii_lowercase)
        
        bem_sucedido, key = obtain_input_answer(x,random_word, bem_sucedido)
        input_ascii = ord(key)

        if input_ascii == 32:

            break

        number_of_types +=1
        input_record = Input(requested=random_word, received=key, duration=tempo_decorrido)
        input_records.append(input_record)  # Adicione o registro à lista
        temponaotenho +=1

        if temponaotenho >= args.max_value:
            break    
          
    for record in input_records:

        print(record.requested)
        print(record.received)
        print(record.duration) 

    print(f"De {number_of_types} tentativas voce acertou em: {bem_sucedido}, com um tempo de jogo de: {tempo_decorrido} segundos.")   
    return number_of_types, bem_sucedido, tempo_decorrido, input_records  


def input_mx( bem_sucedido, tempo_decorrido,word_length): 

    args = arg_init()
    input_records = []
    x=0
    number_of_types=0
    bem_sucedido=0

    while True:

        if args.use_words:
            x=1
            random_word = generate_random_word(word_length)
        else:
            random_word = random.choice(string.ascii_lowercase)
        
        bem_sucedido, key = obtain_input_answer(x,random_word, bem_sucedido)

        input_ascii = ord(key)

        if input_ascii == 32:

            break

        number_of_types +=1
        input_record = Input(requested=random_word, received=key, duration=tempo_decorrido)
        input_records.append(input_record)  # Adicione o registro à lista

        if number_of_types >= args.max_value:
            break    
          
    for record in input_records:

        print(record.requested)
        print(record.received)
        print(record.duration) 

    print(f"De {number_of_types} tentativas voce acertou em: {bem_sucedido}, com um tempo de jogo de: {tempo_decorrido} segundos.")   
    return number_of_types, bem_sucedido, tempo_decorrido, input_records   


def generate_random_word(length):

    word_list = words.words()
    random_word = random.choice(word_list)
    
    return random_word

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

#############################    MAIN    #######################

def main():

    # Variaveis
    data_hora = datetime.now()
    test_start = data_hora.strftime("%Y-%m-%d %H:%M:%S")
    tentativa = 0
    bem_sucedido = 0
    tempo_decorrido =0
    
    #Chamada da função arg_init()
       
    args = arg_init()

    print("Tempo Máximo:", args.max_value)
    print("time mode:", args.use_time_mode)
    print("use words:", args.use_words)

    input("Pressione uma tecla para iniciar o desafio...")

    # Atribuir o length

    if args.use_words:
        word_length = random.randint(2, 10)
    else:
        word_length = 1

    if args.use_time_mode:

        number_of_types, bem_sucedido, tempo_decorrido, input_records = temp_mx( bem_sucedido, tempo_decorrido,word_length)

    else:

        number_of_types, bem_sucedido, tempo_decorrido, input_records = input_mx(bem_sucedido,tempo_decorrido,word_length)  

    # Statistic

    accuracy = bem_sucedido / number_of_types if number_of_types > 0 else 0 


    data_hora_fim = datetime.now()
    test_end = data_hora_fim.strftime("%Y-%m-%d %H:%M:%S")

    result_dict = {
        'accuracy': accuracy,
        'inputs': input_records,
        'number_of_hits': bem_sucedido,
        'test_start': test_start,
        'test_end': test_end,
        'number_of_types': number_of_types,
        }      
    pprint(result_dict)

    
if __name__ == "__main__":
    main()

    # python3 backupinicial.py -utm -mv 10 -uw 