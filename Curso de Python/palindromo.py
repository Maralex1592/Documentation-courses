# -*- coding: utf-8 -*- 
def main():
    car = str(input('Ingresa una palabra: '))
    slice2 = car[::-1]
    print(car, slice2)
    
    if car == slice2:
        print('Es Palindromo')
    else:
        print('No es palindromo')
if __name__ == '__main__':
    main()