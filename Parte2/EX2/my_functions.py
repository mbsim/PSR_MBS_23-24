def isPrime(value):
    for i in range(2,value):
        if value%i == 0:
            print('the number ' + str(value) + ' is not prime because we divide by ' + str(i))
            return False

    return True

def isPerfect(value):

    # Percorrer todos os numeros até ao número em análise
    # para cada umero, ver se é um divisor inteiro
    # Se for, somar num acumulador
    accumulator = 0
    for i in range(1, value):
        if value%i == 0: # its an integer divider
            accumulator = accumulator + i

    # Ver se a soma dos dividores inteiros é igual ao próprio número
    return accumulator == value