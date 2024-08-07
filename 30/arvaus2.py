luku = 42
meni_oikein = False
while not meni_oikein:
    try:
        arvaus_teksti = input('Anna arvauksesi: ')
        arvaus = int(arvaus_teksti)
    except ValueError:
        print('Yritä uudelleen!')
        continue
    else:
        if arvaus < luku:
            print('Se on isompi!')
        elif arvaus > luku:
            print('Se on pienempi!')
        else:
            meni_oikein = True
            print(f'Arvasit oikein, se oli {luku}!')
