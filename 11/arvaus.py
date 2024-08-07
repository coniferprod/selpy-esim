""" Arvauspeli

Tämä ohjelma arpoo satunnaisen kokonaisluvun väliltä 1...100
ja antaa käyttäjän arvata mikä se on. Ohjelma antaa arvauksen
jälkeen vinkin siitä miten lähelle arvaus meni. Käyttäjä saa
arvata niin monta kertaa kuin haluaa.
"""

from random import seed, randint

seed()
luku = randint(1, 100)

MAX_ARVAUKSET = 6
print('Ajattelen jotain lukua väliltä 1...100.')
print(f'Arvaatko mikä se on? Sinulla on {MAX_ARVAUKSET} arvausta.')

meni_oikein = False
arvauksia_jaljella = MAX_ARVAUKSET
while arvauksia_jaljella > 0:
    arvaus_teksti = input('Anna arvauksesi: ')
    arvaus = int(arvaus_teksti)
    arvauksia_jaljella -= 1
    if arvaus < luku:
        print('Se on isompi!')
    elif arvaus > luku:
        print('Se on pienempi!')
    else:
        meni_oikein = True
        break
    if arvauksia_jaljella > 0:
        print(f'Arvauksia jäljellä: {arvauksia_jaljella}')

if meni_oikein:
    print(f'Arvasit oikein, se oli {luku}!')
else:
    print(f'Arvaukset loppuivat! Luku oli {luku}.')
