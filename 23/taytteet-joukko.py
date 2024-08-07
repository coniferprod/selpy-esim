pizzat = {
    1: {'nimi': 'Bolognese',
        'taytteet': ['jauheliha']},
    2: {'nimi': 'Frutti di Mare', 
        'taytteet': ['ananas', 'katkarapu', 'tonnikala']},
    3: {'nimi': 'Americano',
        'taytteet': ['ananas', 'aurajuusto', 'kinkku']},
    4: {'nimi': 'Opera Special', 
        'taytteet': ['kinkku', 'salami', 'tonnikala']},
    5: {'nimi': 'Mexicana', 
        'taytteet': ['ananas', 'pepperoni', 'chili', 
                     'tacokastike']},
    6: {'nimi': 'Julia', 
        'taytteet': ['ananas', 'aurajuusto', 'katkarapu', 
                     'kinkku']},
    7: {'nimi': 'Empire Special', 
        'taytteet': ['katkarapu', 'kinkku', 'mustapippuri', 
                     'salami', 'sipuli', 'tuplajuusto', 
                     'valkosipuli']},
    8: {'nimi': 'Kummisetä',
        'taytteet': ['herkkusieni', 'katkarapu', 'kinkku', 
                     'valkosipuli']},
    9: {'nimi': 'Chicken Hawaii', 
        'taytteet': ['ananas', 'aurajuusto', 'kana']},
    11: {'nimi': 'Romeo', 
         'taytteet': ['ananas', 'aurajuusto', 'katkarapu', 
                      'salami']},
    12: {'nimi': 'Vegetariana', 
         'taytteet': ['herkkusieni', 'oliivi', 'paprika', 
                      'sipuli', 'tomaatti']},
    13: {'nimi': 'Dillinger', 
         'taytteet': ['jauheliha', 'kinkku', 'salami', 
                      'sipuli']},
    14: {'nimi': 'Papa''s Special',
         'taytteet': ['aurajuusto', 'mustapippuri', 'oliivi', 
                      'paprika', 'salami', 'sipuli']},
    15: {'nimi': 'Quattro Stagioni', 
         'taytteet': ['herkkusieni', 'katkarapu', 'kinkku', 
                      'paprika']},
    16: {'nimi': 'Cambretti', 
         'taytteet': ['tuplajuusto', 'katkarapu', 
                      'valkosipuli']},
    17: {'nimi': 'Pepperoni', 
         'taytteet': ['paprika', 'pepperoni', 'tonnikala']},
    19: {'nimi': 'Spicy Hot Crispy', 
         'taytteet': ['mausteinen naudanliha', 'sipuli', 
                      'tomaatti', 'chili']},
    21: {'nimi': 'Finlandia', 
         'taytteet': ['kana', 'katkarapu', 'kinkku', 
                      'salami', 'tonnikala']},
    23: {'nimi': 'Driver''s Special', 
         'taytteet': ['pekoni', 'pepperoni', 'kinkku', 
                      'salami', 'aurajuusto']},
    26: {'nimi': 'Fantasia', 
         'taytteet': [None, None, None, None]}
}

taytteet = set()

for p in pizzat:
    for t in pizzat[p]['taytteet']:
        if t is None:
            continue
        taytteet.add(t)

print(taytteet)
print(len(taytteet))

print(f'Pizzoissamme on yhteensä {len(taytteet)} erilaista täytettä: ', end='')
print(', '.join(sorted(list(taytteet))))
