# -*- coding: utf-8 -*-

car = 'Esternocleidomastoideo'
print(car)
print('')
types =  type(car)
print('type(car)  is::::: {} '.format(types))
size = len(car)
print('len(car) is ::::: {} '.format(size))
replace = car.replace('', ' ')
print('car.replace('', ' ') is::::: {} '.format(replace))
slice1 = car[1:size-1:]
print('car[1:size-1:] is::::: {} '.format(slice1))
slice2 = car[::-1]
print('car[::-1] is::::: {} '.format(slice2))
capital = car.upper()
print('car.upper() is::::: {} '.format(capital))
middle_position = int(size/2)
print('len(car)/2 is::::: {} '.format(middle_position)) 
middle_value = car[middle_position]+'?'
print('car[middle_position]+? is ::::: {}'.format(middle_value))
#book = car[:middle_position] + '?' + car[middle_position:]
number_parts = int(input('Dividir String en cuantas partes? '))
part_start = 0
part_end = 0
for parts in range(0,number_parts):
    position = int(size/number_parts)
    part_end = part_end + position
    book = car[part_start:part_end] + '?'
    part_start = part_start + part_end

print('book = car[:middle_position] + ? + car[middle_position:] is ::::: {}'.format(book))
cut_middle = book.split('?')
print('cut_middle = book.split(?) is ::::: {}'.format(cut_middle))
print('(len(book) is ::::: {}'.format(len(book)))
print('type(book) is ::::: {}'.format(type(book)))
print('len(cut_middle) is ::::: {}'.format(len(cut_middle)))
print('type(cut_middle) is ::::: {}'.format(type(cut_middle)))
