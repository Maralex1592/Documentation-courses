countries = {
    'mexico': 122,
    'colombia': 49,
    'argentina': 43,
    'chile' : 18,
    'peru' : 31
}

while True:
    country = str(input('Type a country name:  ')).lower()
    
    try:
        print('La población de {} es de {}'.format(country, countries[country]))
    except KeyError:
        print('Poblations {} unknow'.format(country))
    
