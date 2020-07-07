# -*- coding: utf-8 -*- 

import random

def main ():
    number_found = False
    random_number = random.randint(0,20)

    while not number_found:
        number = int(input('Adivina el número: '))

        if number == random_number:
            print('Habes adivinado el número')
            number_found = True
        elif number < random_number:
            print('Estuviste por debajo')
        else:
            print('Estuviste por encima')
        pass
if __name__ == '__main__':
    main()