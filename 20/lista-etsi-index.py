nimet = ['Terry', 'Michael', 'John', 
         'Eric', 'Graham', 'Terry']

nimi = 'Eric'
if nimi in nimet:
    indeksi = nimet.index(nimi)
    print(f'{nimi} löytyi kohdasta {indeksi}!')
else:
    print(f'Ei löytynyt: {nimi}')
