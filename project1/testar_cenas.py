
import argparse
from time import time
import datetime
from readchar import readkey
import random
import string
from nltk.corpus import words
from collections import namedtuple
from pprint import pprint


Input = namedtuple('Input', ['requested', 'received', 'duration'])   

def aguardar_tecla():

    print("Pressione uma tecla para começar o desafio...")

    digitado = readkey()

def generate_random_word():

    word_list = words.words()
    return random.choice(word_list)

def generate_random_caracter():

    random_ascii = random.randint(97,122)
    random_caracter = chr(random_ascii)
    return random_caracter

def caracter_function(args):

    input_records = []

    tentativa=0
    bem_sucedido = 0

    start_time = time() 

    while True:

        if tempo_decorrido >= args.max_value:
            break  

        random_ascii = random.randint(97,122)
        random_caracter = chr(random_ascii)

        print(f"Digite: {random_caracter} : ") 

        ti = time()

        key = readkey()

        tf = time()
        duration = tf-ti
        input_ascii = ord(key)

        if input_ascii == 32:

            break

        elif key == random_caracter:
            print(f"Correto, voce inseriu! {key}")
            bem_sucedido += 1
        else:
            print("Incorreto. Tente novamente.")

        tentativa +=1
        input_record = Input(requested=random_caracter, received=key, duration=duration)
        input_records.append(input_record)  # Adicione o registro à lista

    print(f"Em {tentativa} tentativas você acertou em: {bem_sucedido}, em {tempo_decorrido} segundos.")

    for record in input_records:

        print(record.requested)
        print(record.received)
        print(record.duration)

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

def temp_mx(tentativa, bem_sucedido,tempo_decorrido):

    args = arg_init()
    input_records = []

    if not args.use_words:

        print("Função de caracter e tempo maximo:")  
        caracter_function(args) 

    else:   
        print("Função de palavra e tempo maximo:")  

        start_time = time()

        while tempo_decorrido <= args.max_value:

            tempo_atual = time()
            tempo_decorrido = int(tempo_atual - start_time )

            #if tempo_decorrido >= args.max_value:
                #break

            random_word = generate_random_word()
            user_input = input(f"Digite {random_word} : ")

            if user_input.lower() == random_word:

                print(f"Correto, voce inseriu! {user_input}")
                bem_sucedido += 1

            else:

                print("Incorreto!")

            tentativa += 1
            input_record = Input(requested=random_word, received=user_input, duration=tempo_decorrido)
            input_records.append(input_record)  # Adicione o registro à lista
    

        print(f"Em {tentativa} tentativas voce acertou em: {bem_sucedido}, em {tempo_decorrido} segundos.")
        print(f"{tempo_atual}")
        print(f"{start_time}")
        
        for record in input_records:

            print(record.requested)
            print(record.received)
            print(record.duration)   


def input_mx(tentativa, bem_sucedido, tempo_decorrido): 

    args = arg_init()
    input_records = []

    if  args.use_words: 

            print("Função de palavra e input maximo:")  

            start_time = time()

            generate_random_word()
        
            while True:

                tempo_atual = time()

                tempo_decorrido = int(tempo_atual - start_time )

                if tentativa >= args.max_value:
                    break

                random_word = generate_random_word()
                user_input = input(f"Digite {random_word} : ")

                if user_input.lower() == random_word:

                    print(f"Correto, voce inseriu! {user_input}")
                    bem_sucedido += 1

                else:

                    print("Incorreto!")  

                tentativa += 1 
                input_record = Input(requested=random_caracter, received=key, duration=duration)
                input_records.append(input_record)  # Adicione o registro à lista


            
            print(f"De {tentativa} tentativas voce acertou em: {bem_sucedido}, com um tempo de jogo de: {tempo_decorrido} segundos.")        
            
            for record in input_records:

                print(record.requested)
                print(record.received)
                print(record.duration)   

    else:

        tentativa=0
        bem_sucedido = 0

        start_time = time() 

        while True:

            tempo_atual = time()
            tempo_decorrido = int(tempo_atual - start_time )

            if tentativa >= args.max_value:
                break  

            random_ascii = random.randint(97,122)
            random_caracter = chr(random_ascii)

            print(f"Digite: {random_caracter} : ") 

            ti = time()

            key = readkey()

            tf = time()
            duration = tf-ti
            input_ascii = ord(key)

            if input_ascii == 32:

                break

            elif key == random_caracter:
                print(f"Correto, voce inseriu! {key}")
                bem_sucedido += 1
            else:
                print("Incorreto. Tente novamente.")

            tentativa +=1
            input_record = Input(requested=random_caracter, received=key, duration=duration)
            input_records.append(input_record)  # Adicione o registro à lista

        print(f"Em {tentativa} tentativas você acertou em: {bem_sucedido}, em {tempo_decorrido} segundos.")

        for record in input_records:

            print(record.requested)
            print(record.received)
            print(record.duration)   

def statistic(bem_sucedido,tentativa,input_records,tempo_atual,tempo_final):

    accuracy = bem_sucedido / tentativa if tentativa > 0 else 0

    type_average_duration = sum(input_record.duration for input_record in input_records) / tentativa if tentativa > 0 else 0

    type_hit_average_duration = sum(input_record.duration for input_record in input_records if input_record.requested == input_record.received and bem_sucedido > 0) / bem_sucedido if bem_sucedido > 0 else 0

    type_miss_average_duration = sum(input_record.duration for input_record in input_records if input_record.requested != input_record.received and tentativa - bem_sucedido > 0) / (tentativa - bem_sucedido) if tentativa - bem_sucedido > 0 else 0

    result_dict = {
        'accuracy': accuracy,
        'inputs': input_records,
        'number_of_hits': bem_sucedido,
        'number_of_types': tentativa,
        'test_duration': input_records.duration,
        'test_end': tempo_atual,
        'test_start': tempo_final,
        'type_average_duration': type_average_duration,
        'type_hit_average_duration': type_hit_average_duration,
        'type_miss_average_duration': type_miss_average_duration
    }

    pprint(result_dict)    


def main():

    bem_sucedido = 0
    tentativa=0
    tempo_decorrido = 0

    args = arg_init()

    #Printar os argumentos

    print("Tempo Máximo:", args.max_value)
    print("time mode:", args.use_time_mode)
    print("use words:", args.use_words)

    input("Pressione uma tecla para começar o desafio...")
    #aguardar_tecla()

    if args.use_time_mode:

        temp_mx(tentativa, bem_sucedido,tempo_decorrido)

    else:

        input_mx(tentativa, bem_sucedido,tempo_decorrido) 

    statistic(bem_sucedido,tentativa,input_records,tempo_atual,tempo_final)

    

if __name__ == "__main__":
    main()

    # python3 backupinicial.py -utm -mv 10 -uw 







