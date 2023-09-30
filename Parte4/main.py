from time import time
import datetime

max_time = 30
max_inputs = 30


def PrintTime(inicio, fim):
    # Calcula o tempo decorrido
    tempo_decorrido = fim - inicio

    # Formata o tempo em horas, minutos e segundos
    tempo_formatado = str(datetime.timedelta(seconds=tempo_decorrido))

    print("Tempo decorrido:", tempo_formatado)

    # Imprime a data e hora de início e o tempo decorrido
    print(f"Data e hora de início: {datetime.datetime.now()}")
    print(f"Tempo decorrido: {tempo_formatado}")

def time_mode(max_time):
    start_time = time.time()
    while True:
        #  Código aqui
        
        if time.time() - start_time >= max_time:
            break

def input_mode(max_inputs):
    input_count = 0
    while True:
        #  Código aqui
        
        input_count += 1
        if input_count >= max_inputs:
            break


def main():

    # Regista o momento de início
    inicio = time()

    # Menu de escolhas possivies

    while True:

        print("Defina o modo de finalização de teste que pretende :")

        print("1. Opção 1: Tempo Maximo")

        print("2. Opção 2: Numero limite de inputs")

        print("3. Sair")

        escolha = input("Digite o número da opção desejada: ")

        if escolha == "1":

            print("Você escolheu a Opção de Tempo Maximo, para começar o desafio clique num tecla")
            time_mode(max_time)
            

            

        elif escolha == "2":

            print("Você escolheu a Opção Numero limite de inputs, para começar o desafio clique num tecla")

            input_mode(max_inputs)


        elif escolha == "3":

            print("Saiu do menu ...")

            break

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


    

    # Registra o momento de término
    fim = time()
    
    PrintTime(inicio,fim)

if __name__ == "__main__":
    main()





