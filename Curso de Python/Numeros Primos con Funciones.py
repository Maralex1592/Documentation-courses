# -*- coding: utf-8 -*- 
def is_prime(numero):
    if numero < 2:
        return False
    elif numero == 2:
        return True
    elif numero > 2 and numero % 2 == 0:
        return False
    else:
        for i in range(3, numero):
            if numero % i == 0:
                return False
    return True 

def main():
    numero = int(input('Digite un número entero: '))
    result = is_prime(numero)
    if result is True:
        print('El numero es PRIMO')
    else:
        print('El numero NO es Primo')
if __name__ == '__main__':
    main()