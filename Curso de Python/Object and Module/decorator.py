# -*- coding: utf-8 -*- 

def protected(func):
    def wrapper(passw):
        if passw == 'platzy':
            return func()
        else:
            print('Incorrect Password')
    return wrapper

@protected
def protected_func():
    print('Correct Passsword')

if __name__ == '__main__':
    passw = str(input('Type your Pass:: '))
    
    protected_func(passw)
    