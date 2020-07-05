# -*- coding: utf-8 -*- 
import random

IMAGES = ['''
    
   +---+
   |   |
       |
       |
       |
       |
       |
       =======''',''' 

   +---+
   |   |
   O   |
       |
       |
       |
       |
       =======''','''     

   +---+
   |   |
   O   |
   |   |
       |
       |
       |
       =======''','''
       
   +---+
   |   |
   O   |
  /|   |
       |
       |
       |
       =======''','''
              
   +---+
   |   |
   O   |
  /|\  |
       |
       |
       |
       =======''','''
                     
   +---+
   |   |
   O   |
  /|\  |
   |   |
       |
       |
       =======''','''
                            
   +---+
   |   |
   O   |
  /|\  |
   |   |
  /    |
       |
       =======''','''
                            
   +---+
   |   |
   O   |
  /|\  |
   |   |
  / \  |
       |
       =======''','''
    
''']

WORDS = ['SUNDOWN', 'MORNING', 'FIELDS', 'ENOUGHT', 'EVERYITHING', 'CHANGES']

def random_word():
    idx = random.randint(0, len(WORDS) -1)
    return WORDS[idx]

def display_board(hidden_word, tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('')
    print('--------------------------------------------------')

def main():
    word = random_word()
    hidden_word = ['*__*'] * len(word)
    tries = 0

    while True:
        display_board(hidden_word, tries)
        current_letter = str(input('Itenta con una letra  '))

        letter_indexes = []
        for idx in range(len(word)):
            if word[idx] == current_letter:
                letter_indexes.append(idx)
        if len(letter_indexes) == 0:
            tries+=1
            
            if tries == 7:
                display_board(hidden_word, tries)
                print('')
                print('Perdistes! La palabra era {}'.format(word))
                break
                
        else:
            for idx in letter_indexes:
                hidden_word[idx] = current_letter
            letter_indexes = []
        
        try:
            hidden_word.index('*__*')
        except ValueError:
            print('')
            print('Felicidaes! La palabra era {}'.format(word))
        


if __name__ == '__main__':
    print('Bienvenido a la cuenta regresiva por no ser adivino')
    result = main()
    if result == True:
        print("Felicitaciones Chaval habeis adivinado la palabra")
    else:
        print('Im sorry, good look for the next')
