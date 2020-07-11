# -*- coding: utf-8 -*- 
from lamp import DesktopLamp

def main():
    lamp = DesktopLamp(is_turned_on=True)

    while True:
        command = str(input('''
            What do I do? 
            [on] Turn ON
            [off] Turn Off
            [e] Exit
        '''))

        if command == 'on':
            lamp.turn_on()
        elif command == 'off':
            lamp.turn_off()
        elif command == 'e':
            break
        else:
            print('Incorrect Option')
        
if __name__ == '__main__':
    main()