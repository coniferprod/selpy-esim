nimi = ''
p = 0
k = int(input('Anna kuukauden numero (1-12): '))

if k >= 1 and k <= 12:
    if k == 1:
        nimi = 'tammi'
        p = 31
    elif k == 2:
        nimi = 'helmi'
        p = 28  # HUOM.! Ei tunnista karkausvuotta!
    elif k == 3:
        nimi = 'maalis'
        p = 31
    elif k == 4:
        nimi = 'huhti'
        p = 30
    elif k == 5:
        nimi = 'touko'
        p = 31
    elif k == 6:
        nimi = 'kesä'
        p = 30
    elif k == 7:
        nimi = 'heinä'
        p = 31
    elif k == 8:
        nimi = 'elo'
        p = 31
    elif k == 9:
        nimi = 'syys'
        p = 30
    elif k == 10:
        nimi = 'loka'
        p = 31
    elif k == 11:
        nimi = 'marras'
        p = 30
    elif k == 12:
        nimi = 'joulu'
        p = 31

    print(f'{nimi}kuussa on {p} päivää')
else:
    print('Kuukauden numero ei kelpaa!')
    print(f'Piti olla 1-12, mutta oli {k}.')
