from apu import nopanheitto
import textwrap
import time

def alkutekstit():
    teksti = ('Noppapeli yhdelle tai useammalle pelaajalle. '
              'Pelaajat heittävät vuorotellen viittä '
              'tavallista noppaa. Noppien silmäluvut '
              'lasketaan yhteen joka kierroksella. '
              'Voittaja on se, jolla on viiden kierroksen '
              'jälkeen eniten pisteitä.')
    rivit = textwrap.wrap(teksti, width=50)
    for r in rivit:
        print(r)

def peli():
    pelaajat = []

    pelaajien_lkm = int(input('\nAnna pelaajien lukumäärä: '))
    for p in range(pelaajien_lkm):
        nimi = input(f'Anna pelaajan {p+1} nimi: ')
        pelaaja = {'nimi': nimi, 'pisteet': 0}
        pelaajat.append(pelaaja)

    MAX_KIERROKSET = 5
    for kierros in range(MAX_KIERROKSET):
        print(f'*** Kierros {kierros+1} ***\n')
        for p in pelaajat:
            print(f'Heittovuorossa on {p["nimi"]}.')
            time.sleep(0.5)
            heitto = nopanheitto(montako=5)
            print(f'Heiton tulos on {heitto["summa"]} pistettä.')
            p['pisteet'] += heitto['summa']
            print()

    paras_tulos = 0
    paras_pelaaja = None

    for p in pelaajat:
        if p['pisteet'] > paras_tulos:
            paras_tulos = p['pisteet']
            paras_pelaaja = p['nimi']

    print(f'Voittaja on {paras_pelaaja} '
          f'{paras_tulos} pisteellä.')

    print(pelaajat)

def lopputekstit():
    print('\nKiitos pelistä, ja tervetuloa uudelleen '
          'pelaamaan!')

if __name__ == '__main__':
    alkutekstit()
    peli()
    lopputekstit()
