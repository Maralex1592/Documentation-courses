# -*- coding: utf-8 -*-
def foreing_exchange(ammount):
    convert = ammount * 167.36
    return convert

def run ():
    print('Calculadora')
    print('')

    ammount = float(input('Ingres la cantidad a convertir: '))
    result = foreing_exchange(ammount)

    print(result)

if __name__ == '__main__':
    run()