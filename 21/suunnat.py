ilmansuunnat = ('pohjoinen', 'itä', 'etelä', 'länsi')

keskustori = ('Finlayson', 'Hämeensilta', 'Laukontori', 'Hämeenpuisto')

print('Olet Tampereen Keskustorilla.')

for indeksi, suunta in enumerate(ilmansuunnat):
    print(f'Menemällä tästä suuntaan {suunta} ' + 
          f'tulet paikkaan {keskustori[indeksi]}.')
