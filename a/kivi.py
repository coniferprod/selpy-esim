"""
Laske montako kertaa kukin veljeksistä on äänessä
Aleksis Kiven kertomuksessa "Seitsemän veljestä".
Teoksen koko teksti on saatavana Project Gutenbergin
verkkosivuilta: https://www.gutenberg.org/ebooks/11940
Merkistökoodaus on UTF-8.
"""

# Lue kaikki rivit tiedostosta.
with open('11940.txt.utf-8', 'r', encoding='utf-8') as f:
    rivit = f.readlines()

# Puhujat on koodattu nimen mukaan, esim. "EERO." 
# rivin alussa. Seuraavan listan avulla voidaan
# helposti etsiä mainintoja.
nimet = ['Juhani', 'Tuomas', 'Aapo', 'Simeoni', 
         'Timo', 'Lauri', 'Eero']

maininnat = []
for rivi in rivit:
    # Käy läpi kaikki nimet ja tarkista
    # alkaako rivi tekstillä "NIMI."
    for nimi in nimet:
        puhuja = f'{nimi.upper()}.'
        if rivi.startswith(puhuja):
            maininnat.append(nimi)

print(f'Mainintoja yhteensä: {len(maininnat)}')

def laske_kaikki(maininnat):
    """Laske montako kertaa kukin nimi esiintyy."""
    tulos = {}
    for nimi in maininnat:
        if nimi in tulos:
            tulos[nimi] += 1
        else:
            tulos[nimi] = 0

        # Edellinen on sama kuin tämä:
        # tulos[nimi] = tulos.get(nimi, 0) + 1
    return tulos

tulos = laske_kaikki(maininnat)

# Lajittele koko sanakirja avaimia vastaavien arvojen
# mukaan laskevaan järjestykseen (suurin ensin).
lajiteltu_tulos = sorted(tulos.items(), key=lambda x:x[1], 
                         reverse=True)

# Tulosta maininnat sopivasti muotoiltuina.
for v in lajiteltu_tulos:
    print(f'{v[0]}\t{v[1]: >4}')
