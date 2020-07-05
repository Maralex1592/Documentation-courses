
car = str(input('Ingresa una palabra: '))
print(car)
size = len(car)
validate_number = False
while not validate_number:
    number_parts = int(input('Dividir String en cuantas partes? '))
    if number_parts > size:
        print('El numero de partes es superior al tamaño del String y se van a generar valores vacíos')
    else:
        position = int(size/number_parts)
        exte = size%number_parts
        print(exte)
        part_start = 0
        part_end = 0
        book = ''
        for parts in range(0,number_parts):
            part_end = part_end + position
            print(part_start , '' , part_end)
            if exte != 0:
                if parts == number_parts -( exte ):
                    part_end = part_end + 1
                    exte = exte - 1
            if parts == number_parts -1:
                book = book + car[part_start:part_end]
            else:
                book = book + car[part_start:part_end] + '?'
            part_start = part_end
        validate_number = True

print('book = car[:middle_position] + ? + car[middle_position:] is ::::: {}'.format(book))
cut_middle = book.split('?')
print('cut_middle = book.split(?) is ::::: {}'.format(cut_middle))
print('(len(book) is ::::: {}'.format(len(book)))