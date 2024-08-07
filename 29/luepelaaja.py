import json

with open('pelaaja.json') as tiedosto:
    pelaaja = json.load(tiedosto)

print(f'Tervetuloa pelaamaan, {pelaaja["nimi"]}!')
print(f'Sinulla on: ')
for esine in pelaaja["esineet"]:
    print(f'- {esine}')
print(f'Pisteet: {pelaaja["pisteet"]}')
