teksti = input('Anna sähkönkulutus kuukaudessa (kWh): ')
kulutus = float(teksti)

myynnin_perusmaksu = 198.0   # snt/kk
energiamaksu = 7.09 # snt/kWh
siirron_perusmaksu = 477.0 # snt/kk
siirron_energiamaksu = 2.9264 # snt/kWh
vero = 2.79372 # snt/kWh

energia = myynnin_perusmaksu + (kulutus * energiamaksu)
siirto = siirron_perusmaksu + (kulutus * siirron_energiamaksu) + (vero * kulutus)
summa = (energia + siirto) / 100.0

print(f'Laskun yhteissumma = {round(summa, 2)} euroa')
