nimet = ['Terry', 'Michael', 'John', 
         'Eric', 'Graham', 'Terry']

for nimi in nimet:
    tila = 'ei vielä kuollut'
    if nimi == 'Terry':
        tila = 'Jones kuollut, Gilliam elossa'
    elif nimi == 'Graham':
        tila = 'kuollut'
    print(f'{nimi}: {tila}')

