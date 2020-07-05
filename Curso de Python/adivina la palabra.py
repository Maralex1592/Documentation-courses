# -*- coding: utf-8 -*- 
import random


"""class Iguess():

    def __init__(self, WORDS, countdown, selected_word):
        self.WORDS = WORDS
        self.countdown = countdown
        self.selected_word = selected_word

	public Object getSelected_word() {
		return this.selected_word;
	}

	public void setSelected_word(Object selected_word) {
		this.selected_word = selected_word;
	}
"""


WORDS = ['SUNDOWN', 'MORNING', 'FIELDS', 'ENOUGHT', 'EVERYITHING', 'CHANGES']

def validate_letter(letters_used):
    state = False
    while not state:
        letter = str(input('Ingrese una letra a adivinar::: '))
        if letter in letters_used:
            print(letters_used)
            print('Ya habeis utilizado esa letra, no seais cabrón tío')
            state = False
        else:
            letters_used.append(letter)
            state = True
            return(letter)

def spaces_def(selected_word):
    number_letter = len(selected_word)
    spaces = []
    for i in range(number_letter):
        spaces.append('__')
    return(spaces)

def main():
    countdown = 3
    letters_used = []
    select_i_word = random.randint(0, (len(WORDS)-1))
    selected_word = WORDS[select_i_word]
    spaces = spaces_def(selected_word)
    gameOver = len(spaces)
    while countdown > 0:
        if gameOver > 0:
            print('Tiene {} intentos para adivinar {} letras de la palabra \n'.format(countdown, gameOver))
            letter = validate_letter(letters_used)
            lucky = False
            for j in range(len(spaces)):
                if letter ==  selected_word[j]:
                    spaces[j] = letter
                    lucky = True
                    gameOver = gameOver -1
            if lucky == False:
                countdown -= 1
            print(spaces,'\n')
        else:
            return True
    return False

if __name__ == '__main__':
    print('Bienvenido a la cuenta regresiva por no ser adivino')
    result = main()
    if result == True:
        print("Felicitaciones Chaval habeis adivinado la palabra")
    else:
        print('Im sorry, good look for the next')
