# -*- coding: utf-8 -*- 

my_dictionary = {}
my_dictionary['firts_element'] = 'Hello'
my_dictionary['second_element'] = 'Bye'

print(my_dictionary['firts_element'])

print(my_dictionary['second_element'])


notes = {}

notes['math'] = 9
notes['lang'] = 12
notes['rel'] = 5
notes['web'] = 7

#for key in notes:
  #  print(key + '\n')
    
for valuees in notes.values():
    print(valuees)

sum = 0
for key, value in notes.items():
    print('En {} sacó {} '.format(key, value))
    sum += value
print(sum)
long = len(notes.values())
print(long)
print('{} dividido en {} da {}'.format(sum, long, sum/long))