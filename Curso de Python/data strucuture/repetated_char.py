# -*- coding: utf-8 -*- 

"""
"abacabad" c
"abacabaabacaba" _
"abcdefghijklmnopqrstuvwxyziflskecznslkjfabe"d
"bcccccccccccccyb"y
"""

def first_no_repeated(char_secquence):
    seen_letters = {}

    for idx,letter in enumerate(char_secquence):
        if letter not in seen_letters:
            seen_letters[letter] = (idx, 1)
        else:
            seen_letters[letter] = (seen_letters[letter][0], seen_letters[letter][1] + 1)

    final_letters = []
    for key, value in seen_letters.items():
        if value[1] == 1:
            final_letters.append((key, value[0]))
    
    #def sort_order(value):
    #    return[1]

    no_repeated_letter = sorted(final_letters, key=lambda value: value[1])

    if no_repeated_letter:
        return no_repeated_letter[0][0]
    else:
        return '_'

if __name__ == '__main__':
    char_secquence = str(input('Type a secquence please  '))

    result = first_no_repeated(char_secquence)

    if result == '_':
        print('Every character is repeated')
    else:
        print('The first character no reapeated is::: {}'.format(result))
