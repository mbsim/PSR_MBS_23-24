import argparse
from time import time
import datetime
from readchar import readkey
import random
import string
import nltk
from nltk.corpus import words

def time_mode(max_value):
    start_time = time.time()
    while time.time() - start_time < max_value:
        pass
    print("Tempo máximo atingido")

def input_mode(max_value):
    for i in range(max_value):
        user_input = input(f"Digite a entrada {i + 1}: ")
        print(f"Entrada {i + 1}: {user_input}")

def generate_random_word():

    word_list = words.words()
    return random.choice(word_list)

def caracter_function(args):

    tentativa=0
    bem_sucedido = 0

    start_time = time() 

    print("jslkdsjvnkjs")

    while True:

        tempo_atual = time()
        tempo_decorrido = int(tempo_atual - start_time )

        if tempo_decorrido >= args.max_value:
            break  

        random_ascii = random.randint(97,122)
        random_caracter = chr(random_ascii)

        print(f"Digite: {random_caracter} : ") 

            #user_input = input(f"Digite: {random_caracter} : ") 
            #input_ascii = ord(readkey(user_input))
        key = readkey()
        input_ascii = ord(key)

        if input_ascii == 32:

            break

        elif key == random_caracter:
            print("Correto!")
            bem_sucedido += 1
        else:
            print("Incorreto. Tente novamente.")

        tentativa +=1    

    print(f"Em {tentativa} tentativas voce acertou em: {bem_sucedido}, em {tempo_decorrido} segundos.")        

def initial_arguments(args):   

    
    return args.max_value, args.use_time_mode, args.use_words  



def main():

    tentativa=0
    bem_sucedido = 0

    parser = argparse.ArgumentParser(description="Definição do modo de teste")
    parser.add_argument("-utm", "--use_time_mode", action="store_true",
                        help="Tempo máximo em segundos para o modo de tempo ou número máximo de entradas para o modo de número de entradas.")
    parser.add_argument("-mv", "--max_value", type=int,
                        help="Tempo máximo em segundos para o modo de tempo ou número máximo de entradas para o modo de número de entradas.")
    parser.add_argument("-uw", "--use_words", action="store_true",
                        help="Usar o modo de digitação de palavras em vez de digitação de caracteres individuais.")
    
    args = parser.parse_args()

    

    print("Tempo Máximo:", args.max_value)
    print("time mode:", args.use_time_mode)
    print("use words:", args.use_words)

    

    if not args.use_words and args.use_time_mode:

        print("Função de caracter e tempo maximo:")

        start_time = time() 

        while True:

            tempo_atual = time()
            tempo_decorrido = int(tempo_atual - start_time )

            if tempo_decorrido >= args.max_value:
                break

            random_ascii = random.randint(97,122)
            random_caracter = chr(random_ascii)

            user_input = input(f"Digite: {random_caracter} : ") 


            if user_input == random_caracter:
                print("Correto!")
                bem_sucedido += 1
            else:
                print("Incorreto. Tente novamente.")

    elif not args.use_words and not args.use_time_mode: 

        caracter_function(args) 

        
    elif  args.use_words and not args.use_time_mode:

            print("Função de palavra e input maximo:")  

            start_time = time()
            print("Função de palavra")

            generate_random_word()
        

            while True:

                tempo_atual = time()
                tempo_decorrido = int(tempo_atual - start_time )

                if tempo_decorrido >= args.max_value:
                    break

                print(f"tempo decorrido {tempo_decorrido} ")

                random_word = generate_random_word()
                user_input = input(f"Digite {random_word} : ")


                if user_input.lower() == random_word:

                    print("Correto!")
                    bem_sucedido += 1

                else:

                    print("Incorreto!")

    elif   args.use_words and not args.use_time_mode: 

            print("Função de palavra e input maximo:")  

            start_time = time()
            print("Função de palavra")

            generate_random_word()
        

            while True:

                tempo_atual = time()
                tempo_decorrido = int(tempo_atual - start_time )

                if tempo_decorrido >= args.max_value:
                    break

                print(f"tempo decorrido {tempo_decorrido} ")

                random_word = generate_random_word()
                user_input = input(f"Digite {random_word} : ")


                if user_input.lower() == random_word:

                    print("Correto!")
                    bem_sucedido += 1

                else:

                    print("Incorreto!")  

                tentativa += 1      

            

    #if args.use_time_mode:
        #if args.max_value is None:
            #print("Você deve especificar um valor máximo usando -mv para o modo de tempo.")
        #else:
            #time_mode(args.max_value)
    #else:
        #if args.max_value is None:
            #print("Você deve especificar um valor máximo usando -mv para o modo de número de entradas.")
        #else:
            #input_mode(args.max_value)
            

if __name__ == "__main__":
    main()