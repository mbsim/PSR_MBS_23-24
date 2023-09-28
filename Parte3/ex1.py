from cmath import sqrt
import math
from time import time, ctime
import datetime

# Registra o momento de início
inicio = time()
value = 50

# Calcula a raiz quadrada dos números de 0 até 50 milhões
for i in range(1,value):
    r = math.sqrt(i)

fim = time()
    

# Registra o momento de término
#fim = time.time()

# Calcula o tempo decorrido
tempo_decorrido = fim - inicio

# Formata o tempo em horas, minutos e segundos
tempo_formatado = str(datetime.timedelta(seconds=tempo_decorrido))

# Imprime a data e hora de início e o tempo decorrido
print(f"Data e hora de início: {datetime.datetime.now()}")
print(f"Tempo decorrido: {tempo_formatado}")