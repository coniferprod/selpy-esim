import time

def esipesu():
    print('Esipesu')
    time.sleep(0.5)

def varsinainen_pesu(lampotila):
    print(f'Varsinainen pesu, {lampotila} astetta')
    time.sleep(3.0)

def huuhtelu():
    print('Huuhtelu')
    time.sleep(1.0)

def linkous(kierrokset):
    print(f'Linkous, {kierrokset} kierrosta minuutissa')
    time.sleep(1.0)

def hienopesu(on_linkous):
    varsinainen_pesu(30)
    huuhtelu()
    if on_linkous:
        linkous(400)
    print('Valmis')

def kirjopesu():
    esipesu()
    varsinainen_pesu(40)
    huuhtelu()
    linkous(800)
    print('Valmis')

def valkopesu():
    esipesu()
    varsinainen_pesu(60)
    huuhtelu()
    linkous(1200)
    print('Valmis')

print('*** Pesumatic 3000 ***')
while True:
    print('\nPesuohjelman valinta:')
    print('1 - kirjopesu')
    print('2 - valkopesu')
    print('3 - hienopesu ilman linkousta')
    print('4 - hienopesu linkouksella')
    print('0 - lopetus')
    valinta = int(input('\nValitse pesuohjelma 1-4'
                        + ' tai 0=lopetus: '))
    print()
    if valinta == 0:
        break
    elif valinta == 1:
        kirjopesu()
    elif valinta == 2:
        valkopesu()
    elif valinta == 3:
        hienopesu(False)
    elif valinta == 4:
        hienopesu(True)
