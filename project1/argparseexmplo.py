#!/usr/bin/env python
import argparse
from time import time
import datetime

def arg_function():
    # Configurar o parser de argumentos
    parser = argparse.ArgumentParser()
    
    # Adicionar argumentos: | TEMPO MÁXIMO |

    parser.add_argument(
        "tempo_maximo",
        type=int,
        help="Máximo Tempo permitido."
    )

    # Adicionar argumentos: | NUMERO INPUTS |

    parser.add_argument(
        "num_inputs_maximo",
        type=int,
        help="Máximo Número de inputs."
    )

    # Adicionar argumentos: | CARACTER/PALAVRA |

    parser.add_argument(
        "--modo",
        choices=["caracter", "palavra"],
        help="Modo de jogo: caracter único ou de palavra."
    )
    
    # Analisar os argumentos da linha de comando

    args = parser.parse_args()
    
    # Exibição dos valores dos argumentos

    print("Tempo Máximo:", args.tempo_maximo)
    print("Número Máximo de Inputs:", args.num_inputs_maximo)
    print("Modo de jogo:", args.modo)


def Print_Time(inicio, fim):
    #       Calcula o tempo decorrido
    tempo_decorrido = fim - inicio
    #       Formata o tempo em horas, minutos e segundos
    tempo_formatado = str(datetime.timedelta(seconds=tempo_decorrido))
    print("Tempo decorrido:", tempo_formatado)
    #       Imprime a data e hora de início e o tempo decorrido
    #print(f"Data e hora de início: {datetime.datetime.now()}")
    #print(f"Tempo decorrido: {tempo_formatado}")


    


def main():

    arg_function()

    inicio = time()

    #########

    fim = time()
    Print_Time(inicio, fim)

if __name__ == "__main__":
    main()

    # python3 argparseexmplo.py 10 5 --modo palavra 

