luku = 42
meni_oikein = False
while not meni_oikein:
    arvaus_teksti = input('Anna arvauksesi: ')
    arvaus = int(arvaus_teksti)
    if arvaus < luku:
        print('Se on isompi!')
    elif arvaus > luku:
        print('Se on pienempi!')
    else:
        meni_oikein = True
        print(f'Arvasit oikein, se oli {luku}!')
