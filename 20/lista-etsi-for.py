nimet = ['Terry', 'Michael', 'John', 
         'Eric', 'Graham', 'Terry']

indeksi = -1
for nimi in nimet:
    indeksi += 1
    if nimi == 'Eric':
        break

if indeksi == -1:
    print('Ei löytynyt Ericiä')
else:
    print(f'Eric löytyi kohdasta {indeksi}!')
