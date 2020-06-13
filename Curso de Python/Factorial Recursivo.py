# -*- coding: utf-8 -*-
def fact(number):
    if number == 0:
        return 1
    return number * fact(number - 1)

if __name__ == '__main__':
    number = int(input('Digite un numero'))

    result = fact(number)
    print('El factorial de  {} es {} '.format(number,result))