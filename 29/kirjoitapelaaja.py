import json

with open('pelaaja.json') as tiedosto:
    pelaaja = json.load(tiedosto)

pelaaja['pisteet'] += 12
pelaaja['esineet'].remove('kukka')

with open('pelaaja.json', 'w') as tiedosto:
    json.dump(pelaaja, tiedosto, indent=4)
