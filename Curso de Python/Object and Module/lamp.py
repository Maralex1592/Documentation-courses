class DesktopLamp:
    #class Variable
    _LAMPS = ['TURN ON','TURN OFF']

    #Init method is the constructor
    def __init__(self, is_turned_on):
        self._is_turned_on = is_turned_on

    def turn_on(self):
        self._is_turned_on = True
        self._display_image()

    def turn_off(self):
        self._is_turned_on = False
        self._display_image()

    def _display_image(self):
        if self._is_turned_on:
            print(self._LAMPS[0])
        else:
            print(self._LAMPS[1])
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
    