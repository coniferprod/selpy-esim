import csv

pizzat = {}  # tehdään aluksi tyhjä lista

with open('pizzalista.csv') as csv_tiedosto:
    csv_lukija = csv.reader(csv_tiedosto)
    eka_rivi = True
    rivilaskuri = 0
    for rivi in csv_lukija:
        if eka_rivi:  # otsikkorivi, hypätään yli
            eka_rivi = False
            continue
        else:
            numero = int(rivi[0])
            nimi = rivi[1]
            taytteet = set(rivi[2].split('/')) if rivi[2] else set()
            pizzat[numero] = {'nimi': nimi, 'taytteet': taytteet}

pizzanumerot = sorted(list(pizzat.keys()))

for numero in pizzanumerot:
    nimi = pizzat[numero]['nimi']
    taytteet = ', '.join(pizzat[numero]['taytteet'])
    if numero == 26:
        taytteet = 'neljä omavalintaista täytettä'
    print(f'{numero}. {nimi} ({taytteet})')
