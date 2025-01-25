teksti = input('Anna sähkönkulutus kuukaudessa (kWh): ')
kulutus = int(teksti)

myynnin_perusmaksu = 179   # snt/kk
energiamaksu = 6.29 # snt/kWh
siirron_perusmaksu = 398 # snt/kk
siirron_energiamaksu = 3.1868 # snt/kWh
vero = 2.79372 # snt/kWh

energia = myynnin_perusmaksu + (kulutus * energiamaksu)
siirto = siirron_perusmaksu + (kulutus * siirron_energiamaksu) + (vero * kulutus)
summa = (energia + siirto) / 100.0

print(f'Laskun summa = {round(summa, 2)} euroa')
