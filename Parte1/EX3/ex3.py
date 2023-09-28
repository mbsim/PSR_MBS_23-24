from colorama import Fore, Back, Style

#maximum_number = 20

def isPrime(value):

    for i in range(2,value):
        if value%i == 0: #
            # Dois modos de escreve a informação que queremos
            #print("The number" +  + str(value) + "is not prime because we can divide by " +str(i))
            print(f"The number {value} is not prime because we can divide by {i}")
            return False
    return True

def main():

    value = int(input('Ate que numero quer ver se e numero primo? : '))
    print("Starting to compute prime numbers up to " + str(value))

    for i in range(0, value):
        if isPrime(i):
            print('Number '+ Back.YELLOW + str(i) + Style.RESET_ALL + ' is prime.')
        else:
            print('Number ' + Fore.RED + str(i) + Style.RESET_ALL + ' is not prime.')

if __name__ == "__main__":
    main()
