pizzat = {
    1: 'Bolognese',
    2: 'Frutti di Mare',
    3: 'Americano',
    4: 'Opera Special',
    5: 'Mexicana',
    6: 'Julia',
    7: 'Empire Special',
    8: 'Kummisetä',
    9: 'Chicken Hawaii',
    11: 'Romeo',
    12: 'Vegetariana',
    13: 'Dillinger',
    14: 'Papa''s Special',
    15: 'Quattro Stagioni',
    16: 'Cambretti',
    17: 'Pepperoni',
    19: 'Spicy Hot Crispy',
    21: 'Finlandia',
    23: 'Driver''s Special',
    26: 'Fantasia'
}

for numero, nimi in pizzat.items():
    print(f'{numero}. {nimi}')

pizzanumerot = sorted(list(pizzat.keys()))
print(pizzanumerot)

print(f'Listallamme on {len(pizzanumerot)} erilaista pizzaa.')
numero = int(input('Anna pizzan numero: '))
if numero in pizzanumerot:
    nimi = pizzat[numero]
    print(f'OK, tulossa yksi {nimi}!')
else:
    print(f'Pahoittelut, pizzaa numero {numero} ei ole listalla.')
